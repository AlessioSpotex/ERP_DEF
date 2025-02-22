import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'oidocrop')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql+psycopg2://root:root@localhost/erp_def')
    SQLALCHEMY_TRACK_MODIFICATIONS = False