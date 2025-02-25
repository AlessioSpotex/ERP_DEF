from models.database import db

class Widget(db.Model):
    __tablename__ = 'widgets'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=True)
    width = db.Column(db.Integer, default=100)
    height = db.Column(db.Integer, default=100)
    
    # Colonna tenant_id per la relazione
    tenant_id = db.Column(db.Integer, db.ForeignKey('tenants.id'), nullable=False)

    # Relazione con il modello Tenant
    tenant = db.relationship('Tenant', backref='widgets')

    def __repr__(self):
        return f'<Widget {self.title}>'