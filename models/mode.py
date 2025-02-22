from models.database import db

class Mode(db.Model):
    __tablename__ = 'modes'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    is_active = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f'<Mode {self.name}>'