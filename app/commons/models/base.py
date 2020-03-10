from datetime import datetime

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
