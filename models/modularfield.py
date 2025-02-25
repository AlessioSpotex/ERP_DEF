from models.database import db

class FieldType:
    TEXT = 'text'
    NUMBER = 'number'
    DATE = 'date'
    SELECT = 'select'
    CHECKBOX = 'checkbox'
    RELATION = 'relation'

class ModularField(db.Model):
    __tablename__ = 'modular_fields'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    field_type = db.Column(db.String(50), nullable=False, default=FieldType.TEXT)  # Tipo di campo (es. testo, numero, data)
    is_required = db.Column(db.Boolean, default=False)  # Se il campo è obbligatorio
    config = db.Column(db.JSON, nullable=True)  # Configurazione aggiuntiva (es. opzioni di selezione)

    # Collegamento al modulo principale
    modular_id = db.Column(db.Integer, db.ForeignKey('modulars.id'), nullable=False)
    
    def __repr__(self):
        return f'<ModularField {self.name} (Type: {self.field_type})>'