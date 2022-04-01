from os import path
from flask import request, send_file
from flask_restful import Resource
from models import db, Email, EmailSchema

emails_schema = EmailSchema(many=True)

class VistaEmail(Resource):
    def get(self):
        emails = Email.query.all()
        ip = request.remote_addr
        return {"emails": emails_schema.dump(emails, many=True), "ip": ip}, 200