from app.commons.models import BaseModel
from app.settings.extensions import db


class Seed(db.Model, BaseModel):
    __tablename__ = 'seeds'
    next_seed = db.Column(db.Integer, default=1)

    default = 1000

    @classmethod
    def get_next_seed(cls):
        instance = cls.custom_query().with_for_update().first()
        if instance:
            next_seed = instance.next_seed
            instance.update(
                next_seed=next_seed+1,
                commit=True
            )
        else:
            next_seed = cls.default
            cls.add(next_seed=next_seed,commit=True)

        return next_seed
