from flask import current_app
from werkzeug.security import gen_salt

from app.commons.models.base import BaseModel
from app.settings.extensions import db, bcrypt


class User(db.Model, BaseModel):
    __tablename__ = 'users'
    first_name = db.Column(db.String(50), nullable=True)
    middle_name = db.Column(db.String(50), nullable=True)
    last_name = db.Column(db.String(50), nullable=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    primary_phone = db.Column(db.String(20), nullable=True)
    secret = db.Column(db.String(100), nullable=True)
    account_status = db.Column(db.String(50), nullable=False, default='active')
    password = db.Column(db.String(100), nullable=False)
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

    @classmethod
    def add(cls, data, commit=True):
        user = cls()
        user.created_by = ""
        user.updated_by = ""
        for col_name in user.__table__.columns.keys():
            if col_name not in [
                'id', 'deleted', 'created_at', 'updated_at', 'deleted_at'
            ]:
                if col_name == 'password' and 'password' in data:
                    secret = gen_salt(50)
                    user.secret = secret
                    user.password = cls.generate_password(data[col_name], secret)
                elif col_name in data and data[col_name] is not None:
                    setattr(user, col_name, data[col_name])

        if commit is True:
            return user.commit()
        else:
            db.session.add(user)
            return user

    @classmethod
    def generate_password(cls, password, salt):
        password_salt = password + salt
        return bcrypt.generate_password_hash(
            password_salt, rounds=current_app.config.get('BCRYPT_ROUNDS')
        )

    def check_password(self, candidate):
        """ Validate a candidate password with actual password """
        candidate_salt = candidate + self.secret
        return bcrypt.check_password_hash(self.password, candidate_salt)
