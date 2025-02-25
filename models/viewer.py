from models.database import db

class ViewType:
    TABLE = 'table'
    KANBAN = 'kanban'
    LIST = 'list'
    CHART = 'chart'

class Viewer(db.Model):
    __tablename__ = 'viewers'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    view_type = db.Column(db.String(50), nullable=False, default=ViewType.TABLE)

    # Configurazione dinamica della vista: colonne visibili, filtri, ordinamento
    columns = db.Column(db.JSON, nullable=True)  # Colonne selezionate dall'utente per la visualizzazione
    filters = db.Column(db.JSON, nullable=True)  # Filtri personalizzati dell'utente
    sorting = db.Column(db.JSON, nullable=True)  # Ordinamento dei dati (es. {"column": "created_at", "direction": "asc"})

    # Collegamento al modulo principale (Modular) e all'utente che ha creato la vista
    modular_id = db.Column(db.Integer, db.ForeignKey('modulars.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    # Stato attivo o bozza della vista
    is_active = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f'<Viewer {self.name} (Type: {self.view_type})>'