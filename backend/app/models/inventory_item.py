from ..extensions.db import db
from datetime import datetime

class InventoryItem(db.Model):
    __tablename__ = "inventory_items"

    id = db.Column(db.Integer, primary_key=True)
    business_id = db.Column(db.Integer, db.ForeignKey("businesses.id"), nullable=False)

    name = db.Column(db.String(150), nullable=False)
    category = db.Column(db.String(50))  # liquor, beer, wine
    unit = db.Column(db.String(50))      # bottle, keg, oz
    par_level = db.Column(db.Float, default=0)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # relationship
    logs = db.relationship("InventoryLog", backref="item", lazy=True)