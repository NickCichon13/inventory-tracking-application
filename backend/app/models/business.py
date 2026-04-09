from ..extensions.db import db
from datetime import datetime

class Business(db.Model):
    __tablename__ = "businesses"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    address = db.Column(db.String(255))

    created_at = db.Column(db.DateTime, default=datetime.utcnow)