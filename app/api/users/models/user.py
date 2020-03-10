from app.commons.models.base import BaseModel
from app.settings.extensions import db


class User(db.Model, BaseModel):
    __tablename__ = 'users'
    firstName = db.Column(db.String(50), nullable=True)
    middleName = db.Column(db.String(50), nullable=True)
    lastName = db.Column(db.String(50), nullable=True)
    username = db.Column(db.String(50), nullable=True)
    email = db.Column(db.String(50), nullable=True)
    primary_phone = db.Column(db.String(20), nullable=True)
    secret = db.Column(db.String(100), nullable=True)
