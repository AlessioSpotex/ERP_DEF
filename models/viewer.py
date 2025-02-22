from models.database import db

class Viewer(db.Model):
    __tablename__ = 'viewers'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    view_type = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Viewer {self.name}>'