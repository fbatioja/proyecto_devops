from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields

db = SQLAlchemy()


class Email(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(320), nullable=False)
    app_uuid = db.Column(db.String(100), nullable=False)
    blocked_reason = db.Column(db.String(255))
    blocker_ip = db.Column(db.String(15))
    blocked_date = db.Column(db.String(10))


class EmailSchema(Schema):
    id = fields.Int(dump_only=True)
    email = fields.Str()
    app_uuid = fields.Str()
    blocked_reason = fields.Str()
    blocker_ip = fields.Str()
    blocked_date = fields.Str()
