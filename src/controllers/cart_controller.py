from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from init import db
from models.cart import Cart, cart_schema

cart_bp = Blueprint("cart", __name__, url_prefix="/cart")

# /cart - GET - fetch all cart
@cart_bp.route("/")
def get_all_cart():
    stmt = db.select(Cart).order_by(Cart.date.desc())
    cart = db.session.scalars(stmt)
    return cart_schema.dump(cart)





