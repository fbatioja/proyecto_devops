from flask import Flask
from flask_restful import Api
from views import VistaEmail, VistaDetailEmail, VistaMicroService
from models import db
import os

aplication = Flask(__name__)

if 'RDS_HOSTNAME' in os.environ:
    engine = os.environ['DB_ENGINE'] if os.environ['DB_ENGINE'] else 'mysql+pymysql'
    dbUser = os.environ['RDS_USERNAME']
    dbPassword = os.environ['RDS_PASSWORD']
    dbHost = os.environ['RDS_HOSTNAME']
    dbName = os.environ['RDS_DB_NAME']
    dbPort = os.environ['RDS_PORT']
    aplication.config['SQLALCHEMY_DATABASE_URI'] = f"{engine}://{dbUser}:{dbPassword}@{dbHost}:{dbPort}/{dbName}"
else:
    aplication.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///black-list.db'

aplication.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
aplication.config['PROPAGATE_EXCEPTIONS'] = True
app_context = aplication.app_context()
app_context.push()

db.init_app(aplication)

@aplication.before_first_request
def create_tables():
    db.create_all()

api = Api(aplication)
api.add_resource(VistaEmail, '/blacklists')
api.add_resource(VistaDetailEmail, '/blacklists/<string:email>')
api.add_resource(VistaMicroService, '/ms-options')