from flask import Blueprint, render_template, redirect, url_for, session, g, request
from models import Tenant, User, Kanban, Widget
from werkzeug.security import check_password_hash
from auth import check_user_authentication  # Importa la funzione di autenticazione

pages_bp = Blueprint('pages', __name__, url_prefix='/<tenant_name>')

# Rotta GET per visualizzare la pagina di login --------------------------------------------------------------------------------------
@pages_bp.route('/login', methods=['GET'])
def login_page(tenant_name):
    tenant = Tenant.query.filter_by(name=tenant_name).first()
    if not tenant:
        return "Tenant non trovato", 404
    return render_template('login.html', tenant=tenant)

# Rotta POST per processare il form di login --------------------------------------------------------------------------------------
@pages_bp.route('/login', methods=['POST'])
def login_post(tenant_name):
    tenant = Tenant.query.filter_by(name=tenant_name).first()
    if not tenant:
        return "Tenant non trovato", 404

    username = request.form.get('username')
    password = request.form.get('password')

    # Autenticazione legata al tenant
    user = User.query.filter_by(username=username, tenant_id=tenant.id).first()
    if not user or not check_password_hash(user.password, password):
        return "Credenziali errate", 401

    # Salva l'utente nella sessione
    session['user_id'] = user.id
    session['tenant_name'] = tenant_name

    # Reindirizza direttamente alla dashboard
    return redirect(url_for('pages.homepage', tenant_name=tenant_name))

# Rotta per la pagina di caricamento della sessione --------------------------------------------------------------------------------------
@pages_bp.route('/admin/sessione')
def sessione(tenant_name):
    username = check_user_authentication()
    if isinstance(username, str):
        return render_template('admin/sessione.html', tenant_name=tenant_name, username=username)
    return username

# Rotta per la dashboard con sessione e tenant --------------------------------------------------------------------------------------
@pages_bp.route('/admin/pages/home', methods=['GET'])
def homepage(tenant_name):
    username = check_user_authentication()
    if isinstance(username, str):
        widgets = Widget.query.filter_by(tenant_id=g.tenant.id).all()
        kanban_tasks = Kanban.query.filter_by(tenant_id=g.tenant.id).all()

        data = {
            'tenant': g.tenant,
            'user': g.user,
            'widgets': widgets,
            'kanbanTasks': kanban_tasks,
            'username': username
        }

        return render_template('admin/pages/home.html', **data)
    return username

# Rotta per il logout --------------------------------------------------------------------------------------
@pages_bp.route('/logout')
def logout_page(tenant_name):
    session.clear()
    return redirect(url_for('pages.login_page', tenant_name=tenant_name))