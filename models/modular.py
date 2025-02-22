from models.database import db

class Modular(db.Model):
    __tablename__ = 'modulars'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<Modular {self.name}>'