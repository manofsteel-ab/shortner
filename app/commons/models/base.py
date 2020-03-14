from datetime import datetime
from sqlalchemy.exc import IntegrityError

from app.settings.extensions import db


class BaseModel:
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    created_at = db.Column(
        db.DateTime, default=datetime.utcnow, nullable=False
    )
    created_by = db.Column(db.Integer(), nullable=True)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow,
        nullable=False
    )
    updated_by = db.Column(db.Integer(), nullable=True)
    deleted_at = db.Column(db.DateTime, nullable=True)

    @classmethod
    def custom_query(cls):
        return db.session.query(cls)

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
        ignore_columns = ['id', 'createdAt', 'updatedAt', 'deletedAt']
        for col_name in self.__table__.columns.keys():
            if col_name not in ignore_columns and kwargs.get(col_name) is not None:
                setattr(self, col_name, kwargs.get(col_name))
        return self

    def delete(self, commit=True):
        self.deleted_at = datetime.utcnow()
        if commit is True:
            return self.commit()
        else:
            return self

    def add_to_session(self):
        db.session.add(self)

