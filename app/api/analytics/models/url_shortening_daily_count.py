from app.commons.models.base import BaseModel
from app.settings.extensions import db


class UrlShorteningDailyCount(db.Model, BaseModel):
    __tablename__ = 'url_shortening_daily_count'
    date = db.Column(db.DateTime, nullable=False, index=True)
    success_count = db.Column(db.Integer, nullable=False, default=0)
    failed_count = db.Column(db.Integer, nullable=False, default=0)
