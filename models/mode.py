from models.database import db

class Mode(db.Model):
    __tablename__ = 'modes'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    is_active = db.Column(db.Boolean, default=True)

    # Nuovi campi per la funzionalità delle modalità in un ERP
    mode_type = db.Column(db.String(50), nullable=False, default='standard')  # Esempio: 'standard', 'advanced', 'debug'
    description = db.Column(db.Text, nullable=True)  # Descrizione dettagliata della modalità
    settings = db.Column(db.JSON, nullable=True)  # Impostazioni dinamiche specifiche della modalità
    
    # Collegamento con il Tenant per il multitenant
    tenant_id = db.Column(db.Integer, db.ForeignKey('tenants.id'), nullable=False)

    def __repr__(self):
        return f'<Mode {self.name} (Type: {self.mode_type}) - Active: {self.is_active}>'