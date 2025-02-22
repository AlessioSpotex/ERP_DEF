from models.database import db

class Kanban(db.Model):
    __tablename__ = 'kanbans'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    position = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f'<Kanban {self.title}>'