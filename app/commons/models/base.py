from datetime import datetime
from uuid import uuid4

from sqlalchemy import false
from sqlalchemy.exc import IntegrityError

from app.settings.extensions import db


class BaseModel:
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    createdAt = db.Column(
        db.DateTime, default=datetime.utcnow, nullable=False
    )
    createdBy = db.Column(db.Integer(), nullable=True)
    updatedAt = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow,
        nullable=False
    )
    updatedBy = db.Column(db.Integer(), nullable=True)
    deletedAt = db.Column(db.DateTime, nullable=True)
    deleteToken = db.Column(db.String(100), nullable=False, default='NA')

    @classmethod
    def custom_query(cls):
        return db.session.query(cls).filter(cls.deleteToken != 'NA')

    def commit(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self
        except IntegrityError:
            db.session.rollback()
            raise Exception("Integrity issue")
        except Exception:
            db.session.rollback()
            raise

    @classmethod
    def add(cls, **kwargs):
        obj = cls()
        obj.assign_attributes(**kwargs)
        obj.add_to_session()
        if kwargs.get('commit'):
            return obj.commit()
        return obj

    def update(self, **kwargs):
        self.assign_attributes(**kwargs)
        self.add_to_session()
        if kwargs.get('commit'):
            return self.commit()
        else:
            return self

    def assign_attributes(self, **kwargs):
        ignore_columns = ['id', 'created_at', 'updated_at', 'deleted_at']
        for col_name, value in kwargs.items():
            if col_name not in ignore_columns:
                if hasattr(self, col_name) and value is not None:
                    setattr(self, col_name, value)
        return self

    def delete(self, commit=True):
        self.deletedAt = datetime.utcnow()
        self.deleteToken = str(uuid4())
        if commit is True:
            return self.commit()
        else:
            return self

    def add_to_session(self):
        db.session.add(self)

