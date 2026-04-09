from flask import Blueprint, request, jsonify
from ..extensions.db import db
from ..models.inventory_item import InventoryItem
from ..models.inventory_log import InventoryLog

inventory_bp = Blueprint("inventory", __name__)

@inventory_bp.route("/inventory-items", methods=["POST"])
def create_inventory_item():
    data = request.get_json()

    item = InventoryItem(
        business_id=data.get("business_id"),
        name=data.get("name"),
        category=data.get("category"),
        unit=data.get("unit"),
        par_level=data.get("par_level", 0)
    )

    db.session.add(item)
    db.session.commit()

    return jsonify({"message": "Item created", "id": item.id}), 201

@inventory_bp.route("/inventory-items", methods=["GET"])
def get_inventory_items():
    items = InventoryItem.query.all()

    result = []
    for item in items:
        result.append({
            "id": item.id,
            "name": item.name,
            "category": item.category,
            "unit": item.unit,
            "par_level": item.par_level
        })

    return jsonify(result), 200

@inventory_bp.route("/inventory-logs", methods=["POST"])
def log_inventory_change():
    data = request.get_json()

    log = InventoryLog(
        inventory_item_id=data.get("inventory_item_id"),
        change_type=data.get("change_type"),
        quantity_change=data.get("quantity_change"),
        note=data.get("note")
    )

    db.session.add(log)
    db.session.commit()

    return jsonify({"message": "Log created"}), 201

