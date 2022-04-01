from flask import Flask
from flask_restful import Api
from views import VistaEmail
from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///black-list.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app_context = app.app_context()
app_context.push()

db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

api = Api(app)
api.add_resource(VistaEmail, '/blacklists')