from app.commons.models.base import BaseModel
from app.settings.extensions import db


class User(db.Model, BaseModel):
    __tablename__ = 'users'
    first_name = db.Column(db.String(50), nullable=True)
    middle_name = db.Column(db.String(50), nullable=True)
    last_name = db.Column(db.String(50), nullable=True)
    username = db.Column(db.String(50), nullable=True)
    email = db.Column(db.String(50), nullable=True)
    primary_phone = db.Column(db.String(20), nullable=True)
    secret = db.Column(db.String(100), nullable=True)
    account_status = db.Column(db.String(50), nullable=False, default='active')
    delete_token = db.Column(db.String(100), nullable=False, default='NA')

    __table_args__ = (
        db.UniqueConstraint(
            'username', 'delete_token',
            name='uq_users_username_delete_token'
        ),
        db.UniqueConstraint(
            'email', 'delete_token', name='uq_users_email_delete_token'
        ),
    )
