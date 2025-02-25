from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models import database, Modular, ModularField, ModularRecord, ModularWorkflow, Tenant
from auth import check_user_authentication

modular_bp = Blueprint('modular', __name__, url_prefix='/<tenant_name>/modular')

# Rotta GET per visualizzare il form di creazione del modulo
@modular_bp.route('/create', methods=['GET'])
def create_module_page(tenant_name):
    user = check_user_authentication()
    if not user:
        return redirect(url_for('pages.login_page', tenant_name=tenant_name))
    
    return render_template('admin/modular/create_module.html', tenant_name=tenant_name, user=user)

# Rotta POST per gestire la creazione del modulo
@modular_bp.route('/create', methods=['POST'])
def create_module(tenant_name):
    user = check_user_authentication()
    if not user:
        return redirect(url_for('pages.login_page', tenant_name=tenant_name))
    
    module_name = request.form.get('module_name')
    module_description = request.form.get('module_description')
    modular_type = request.form.get('modular_type', 'table')
    is_active = request.form.get('is_active') == 'on'
    is_template = request.form.get('is_template') == 'on'
    
    # Creazione della configurazione JSON a partire dai campi chiave-valore
    keys = request.form.getlist('config_keys[]')
    values = request.form.getlist('config_values[]')
    module_config = dict(zip(keys, values))
    
    # Creazione del nuovo modulo
    new_module = Modular(
        name=module_name,
        description=module_description,
        modular_type=modular_type,
        config=module_config,
        is_active=is_active,
        is_template=is_template,
        tenant_id=session['tenant_id']
    )
    
    database.session.add(new_module)
    database.session.commit()
    
    flash('Modulo creato con successo!', 'success')
    return redirect(url_for('pages.homepage', tenant_name=tenant_name))