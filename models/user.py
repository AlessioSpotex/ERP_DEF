from models.database import db

class UserRole:
    ADMIN = 'admin'
    USER = 'user'
    GUEST = 'guest'

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(50), default=UserRole.USER, nullable=False)
    is_active = db.Column(db.Boolean, default=True)

    # Nuovi campi aggiunti
    nome = db.Column(db.String(100), nullable=False)
    cognome = db.Column(db.String(100), nullable=False)
    profilo_foto = db.Column(db.String(255), default='images/default_avatar.png')

    # Collegamento con il Tenant
    tenant_id = db.Column(db.Integer, db.ForeignKey('tenants.id'), nullable=False)

    def __repr__(self):
        return f'<User {self.username} ({self.nome} {self.cognome}) - Role: {self.role}>'