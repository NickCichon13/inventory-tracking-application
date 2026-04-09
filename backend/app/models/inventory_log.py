from ..extensions.db import db
from datetime import datetime

class InventoryLog(db.Model):
    __tablename__ = "inventory_logs"

    id = db.Column(db.Integer, primary_key=True)
    inventory_item_id = db.Column(db.Integer, db.ForeignKey("inventory_items.id"), nullable=False)

    change_type = db.Column(db.String(50))  # add, subtract, waste, sale
    quantity_change = db.Column(db.Float, nullable=False)

    note = db.Column(db.String(255))

    created_at = db.Column(db.DateTime, default=datetime.utcnow)