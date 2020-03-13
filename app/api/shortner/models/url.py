from app.commons.models.base import BaseModel
from app.settings.extensions import db


class Url(db.Model, BaseModel):
    __tablename__ = 'urls'

    longUrl = db.Column(db.Text(), nullable=False)
    urlHash = db.Column(db.String(200), nullable=False, index=True)
    expiresAt = db.Column(db.DateTime, nullable=False)
    hitCount = db.Column(db.Integer, nullable=False, default=0)

    @classmethod
    def fetch_by_hash(cls, hash_val):
        query = cls.custom_query().filter(
            cls.urlHash == hash_val
        )
        return query
