from models.database import db

class ModularType:
    TABLE = 'table'
    KANBAN = 'kanban'
    TASK = 'task'
    WORKFLOW = 'workflow'
    FORM = 'form'
    DASHBOARD = 'dashboard'

class Modular(db.Model):
    __tablename__ = 'modulars'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)
    
    # Tipologia di modulo (tabelle, kanban, task, flussi, form, dashboard, ecc.)
    modular_type = db.Column(db.String(50), nullable=False, default=ModularType.TABLE)

    # Configurazioni dinamiche in formato JSON per supportare la creazione autonoma
    config = db.Column(db.JSON, nullable=True)

    # Collegamento al tenant per la logica multitenant
    tenant_id = db.Column(db.Integer, db.ForeignKey('tenants.id'), nullable=False)

    # Stato attivo o bozza del modulo
    is_active = db.Column(db.Boolean, default=True)
    is_template = db.Column(db.Boolean, default=False)  # Se il modulo è un template riutilizzabile

    def __repr__(self):
        return f'<Modular {self.name} (Type: {self.modular_type}) - Active: {self.is_active}>'
    
    #Perfetto! Se desideri che l’utente possa creare moduli personalizzati con tabelle, kanban, tasks, flussi, e altro, il modello Modular deve essere flessibile, supportare strutture dinamiche e integrazioni con altre entità dell’ERP.