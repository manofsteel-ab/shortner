from app.commons.models.base import BaseModel
from app.settings.extensions import db


class Url(db.Model, BaseModel):
    __tablename__ = 'urls'

    longUrl = db.Column(db.Text(), nullable=False)
    shortUrl = db.Column(db.String(200), nullable=False)
    expiresAt = db.Column(db.DateTime, nullable=False)
    hitCount = db.Column(db.Integer, nullable=False, default=0)
