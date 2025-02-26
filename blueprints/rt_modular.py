from flask import Blueprint, render_template, request, redirect, url_for, flash, session, jsonify
from models.database import db 
from models import Modular, ModularField, ModularRecord, ModularWorkflow, Tenant
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

    # Recupera l'ID del tenant dalla sessione o dal database
    tenant_id = session.get('tenant_id')
    if not tenant_id:
        tenant = Tenant.query.filter_by(name=tenant_name).first()
        if tenant:
            tenant_id = tenant.id
        else:
            flash('Errore: Tenant non trovato!', 'error')
            return redirect(url_for('pages.homepage', tenant_name=tenant_name))
    
    # Creazione del nuovo modulo
    new_module = Modular(
        name=module_name,
        description=module_description,
        modular_type=modular_type,
        is_active=is_active,
        is_template=is_template,
        tenant_id=tenant_id
    )
    
    db.session.add(new_module)
    db.session.commit()

    # Creazione dei campi del modulo (ModularFields)
    field_names = request.form.getlist('field_names[]')
    field_types = request.form.getlist('field_types[]')
    field_required = request.form.getlist('field_required[]')
    field_configs = request.form.getlist('field_configs[]')
    
    for name, ftype, required, config in zip(field_names, field_types, field_required, field_configs):
        field_config = None
        if config:
            try:
                field_config = jsonify.loads(config)
            except ValueError:
                flash(f'Configurazione del campo "{name}" non valida.', 'error')
        
        new_field = ModularField(
            name=name,
            field_type=ftype,
            is_required=(required == 'on'),
            config=field_config,
            modular_id=new_module.id
        )
        db.session.add(new_field)

    db.session.commit()
    
    flash('Modulo creato con successo!', 'success')
    return redirect(url_for('pages.homepage', tenant_name=tenant_name))

# API per ottenere i moduli dinamicamente tramite AJAX
@modular_bp.route('/get_modules', methods=['GET'])
def get_modules(tenant_name):
    tenant_id = session.get('tenant_id')
    
    if not tenant_id:
        return jsonify({'error': 'Tenant ID non trovato nella sessione'}), 400
    
    modules = Modular.query.filter_by(tenant_id=tenant_id, is_active=True).all()
    module_list = [{'id': module.id, 'name': module.name, 'type': module.modular_type} for module in modules]
    
    return jsonify(module_list)

# Rotte dinamiche per visualizzare i moduli in base alla tipologia
@modular_bp.route('/view/<modular_type>/<int:module_id>', methods=['GET'])
def view_module(tenant_name, modular_type, module_id):
    user = check_user_authentication()
    if not user:
        return redirect(url_for('pages.login_page', tenant_name=tenant_name))
    
    module = Modular.query.filter_by(id=module_id, tenant_id=session['tenant_id']).first()
    if not module:
        flash('Modulo non trovato.', 'error')
        return redirect(url_for('pages.homepage', tenant_name=tenant_name))

    # Recupera i campi associati al modulo
    fields = ModularField.query.filter_by(modular_id=module.id).all()
    
    # Recupera i record della tabella associati al modulo
    records = ModularRecord.query.filter_by(modular_id=module.id).all()
    
    template_map = {
        'table': 'admin/modular/view_table.html',
        'kanban': 'admin/modular/view_kanban.html',
        'task': 'admin/modular/view_task.html',
        'workflow': 'admin/modular/view_workflow.html',
        'form': 'admin/modular/view_form.html',
        'dashboard': 'admin/modular/view_dashboard.html',
    }

    template = template_map.get(modular_type.lower(), 'admin/modular/view_default.html')
    
    return render_template(template, module=module, fields=fields, records=records, tenant_name=tenant_name, user=user)