from app.commons.models import BaseModel
from app.settings.extensions import db


class UserRole(db.Model, BaseModel):
    __tablename__ = 'user_roles'

    role_id = db.Column(db.String(20), nullable=False)
    user_id = db.Column(
        db.Integer, db.ForeignKey('users.id'), nullable=False
    )
    user = db.relationship('User')

    @classmethod
    def fetch_by_user_id(cls, user_id):
        return cls.custom_query().filter(cls.user_id == user_id)
