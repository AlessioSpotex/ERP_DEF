from models.database import db

class WorkflowStatus:
    PENDING = 'pending'
    IN_PROGRESS = 'in_progress'
    COMPLETED = 'completed'
    CANCELLED = 'cancelled'

class ModularWorkflow(db.Model):
    __tablename__ = 'modular_workflows'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    status = db.Column(db.String(50), default=WorkflowStatus.PENDING)  # Stato del flusso di lavoro
    steps = db.Column(db.JSON, nullable=True)  # Definisce i passaggi del workflow in formato JSON

    # Collegamento al modulo principale e al tenant
    modular_id = db.Column(db.Integer, db.ForeignKey('modulars.id'), nullable=False)
    tenant_id = db.Column(db.Integer, db.ForeignKey('tenants.id'), nullable=False)

    def __repr__(self):
        return f'<ModularWorkflow {self.name} - Status: {self.status}>'