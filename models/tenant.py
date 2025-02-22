from models.database import db

class Tenant(db.Model):
    __tablename__ = 'tenants'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    domain = db.Column(db.String(255), unique=True, nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    
    # Relazione con gli utenti
    users = db.relationship('User', backref='tenant', lazy=True)

    def __repr__(self):
        return f'<Tenant {self.name}>'