from datetime import date
from flask import request
from flask_restful import Resource
from models import db, Email, EmailSchema

email_schema = EmailSchema()
emails_schema = EmailSchema(many=True)

secret = "AgileMates-DevOps"


class VistaEmail(Resource):   
    def post(self):
        authorization = request.headers['Authorization'].split(' ')
        if not (authorization[1] == secret):
            return {"Unauthorized"}, 401
        else:
            ip = request.remote_addr
            dateTimeObj = date.today()
            timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S.%f)")
            new_email = Email(email=request.json["email"], app_uuid=request.json["app_uuid"], blocked_reason=request.json["blocked_reason"], blocker_ip=ip, blocked_date=timestampStr)
            db.session.add(new_email)
            db.session.commit()
            return {"message": "Registration successfully created"}, 200

class VistaDetailEmail(Resource):
    def get(self, email):
        authorization = request.headers['Authorization'].split(' ')
        if not (authorization[1] == secret):
            return {"Unauthorized"}, 401
        else:
            if email is None:
                return {"message": "Ingrese un email válido"}, 400
            else:
                email_bl = Email.query.filter_by(email = email).first()
                if email_bl is None:
                    return {"message": "El email no está en la lista negra"}, 200
                return {"message": "El email se encuentra en la lista negra", "email": email_schema.dump(email_bl)}, 412

class VistaMicroService(Resource):
    def get(self):
        emails = Email.query.all()
        return {"emails": emails_schema.dump(emails, many=True)}, 200

    def delete(self):
        Email.query.delete()
        db.session.commit()
        emails = Email.query.all()
        return {"message":"Base de datos borrada","emails": emails_schema.dump(emails, many=True)}, 200
