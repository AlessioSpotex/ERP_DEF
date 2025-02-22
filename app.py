from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

from models.database import db
from models import User, Modular, Mode, Kanban, Widget, Viewer, Editor, Tenant
from blueprints.__init import blueprints_register

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'postgresql+psycopg2://root:root@localhost/erp_def')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inizializza il database
db.init_app(app)
migrate = Migrate(app, db)

# Registra tutti i blueprint
for bp in blueprints_register:
    app.register_blueprint(bp)

if __name__ == '__main__':
    app.run(debug=True)