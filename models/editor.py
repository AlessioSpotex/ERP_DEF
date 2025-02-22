from models.database import db

class Editor(db.Model):
    __tablename__ = 'editors'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    version = db.Column(db.String(20), nullable=True)

    def __repr__(self):
        return f'<Editor {self.name}>'