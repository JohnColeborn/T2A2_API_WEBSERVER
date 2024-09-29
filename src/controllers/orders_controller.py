from flask import Blueprint

from init import db
from models.orders import Orders, orders_schema

orders_bp = Blueprint("orders", __name__, url_prefix="/orders")

# /orders - GET - fetch all orders
@orders_bp.route("/")
def get_all_orders():
    stmt = db.select(Orders)
    orders = db.session.scalars(stmt)
    return orders_schema.dump(orders)

