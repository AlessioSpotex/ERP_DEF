from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from dotenv import load_dotenv

# Carica le variabili d'ambiente dal file .env
load_dotenv()

# Inizializza l'app Flask
app = Flask(__name__)

# Configura la chiave segreta per le sessioni Flask
app.secret_key = os.getenv('SECRET_KEY')

# Configura il database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'postgresql+psycopg2://root:root@localhost/erp_def')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inizializza il database e la migrazione
from models.database import db
from models import User, Modular, Mode, Kanban, Widget, Viewer, Editor, Tenant, ModularField, ModularRecord, ModularWorkflow
db.init_app(app)
migrate = Migrate(app, db)

# Registra tutti i blueprint
from blueprints.__init import blueprints_register
for bp in blueprints_register:
    app.register_blueprint(bp)

if __name__ == '__main__':
    app.run(debug=True)