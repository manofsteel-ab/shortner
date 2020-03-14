from app.commons.models.base import BaseModel
from app.settings.extensions import db


class Shortner(db.Model, BaseModel):
    __tablename__ = 'shortner'

    long_url = db.Column(db.Text(), nullable=False)
    url_hash = db.Column(db.String(20), nullable=False, index=True)
    expires_at = db.Column(db.DateTime, nullable=False)
    hit_count = db.Column(db.Integer, nullable=False, default=0)
    delete_token = db.Column(db.String(100), nullable=False, default='NA')

    __table_args__ = (
        db.UniqueConstraint(
            'url_hash', 'delete_token',
            name='uq_shortner_url_hash_delete_token'
        ),
    )

    @classmethod
    def fetch_by_hash(cls, hash_val):
        query = cls.custom_query().filter(
            cls.url_hash == hash_val
        )
        return query
