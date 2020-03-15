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

    def to_dict(self):
        """
        Dictionary representation of the object.
        By default all the columns are read, these can be extended by,
        setting an attribute `hybrid_properties` in the model and also can be
        filtered for sensitive fields using `hidden_fields`
        """
        data = dict()
        hidden_fields = []
        fields = self.__table__.columns.keys()

        if hasattr(self, 'hidden_fields'):
            hidden_fields = self.hidden_fields

        if hasattr(self, 'hybrid_properties'):
            fields += self.hybrid_properties

        for field in fields:
            if field not in hidden_fields:
                if hasattr(self, field):
                    data[field] = getattr(self, field)
                    if type(data[field]) == datetime:
                        data[field] = str(data[field])
                    elif isinstance(data[field], BaseModel):
                        data[field] = data[field].to_dict()
        return data


