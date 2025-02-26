from app import app, db
from models import User, Tenant, Modular, Mode, Kanban, Widget, Viewer, Editor

with app.app_context():
    try:
        # Elimina tutti i record dalle tabelle del database
        #db.session.query(User).delete()
        #db.session.query(Tenant).delete()
        db.session.query(Modular).delete()
        db.session.query(Mode).delete()
        db.session.query(Kanban).delete()
        db.session.query(Widget).delete()
        db.session.query(Viewer).delete()
        db.session.query(Editor).delete()
        
        db.session.commit()
        print("Tutte le tabelle sono state svuotate con successo!")
    
    except Exception as e:
        db.session.rollback()
        print(f"Errore durante la pulizia del database: {e}")