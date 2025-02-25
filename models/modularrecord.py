from models.database import db

class ModularRecord(db.Model):
    __tablename__ = 'modular_records'
    
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.JSON, nullable=False)  # Dati memorizzati in formato JSON

    # Collegamento al modulo a cui appartengono i dati
    modular_id = db.Column(db.Integer, db.ForeignKey('modulars.id'), nullable=False)

    # Collegamento al tenant per il multitenant
    tenant_id = db.Column(db.Integer, db.ForeignKey('tenants.id'), nullable=False)

    def __repr__(self):
        return f'<ModularRecord ID: {self.id} - Modular ID: {self.modular_id}>'