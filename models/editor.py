from models.database import db

class Editor(db.Model):
    __tablename__ = 'editors'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    version = db.Column(db.String(20), nullable=True)

    # Nuovi campi per la funzionalità dell'editor in un ERP
    editor_type = db.Column(db.String(50), nullable=False, default='text')  # Esempio: 'text', 'code', 'wysiwyg', 'spreadsheet'
    config_options = db.Column(db.JSON, nullable=True)  # Configurazioni aggiuntive in formato JSON
    is_active = db.Column(db.Boolean, default=True)  # Stato attivo o disattivo dell'editor

    # Collegamento con il Tenant per il multitenant
    tenant_id = db.Column(db.Integer, db.ForeignKey('tenants.id'), nullable=False)
    
    def __repr__(self):
        return f'<Editor {self.name} (Version: {self.version}) - Type: {self.editor_type}>'