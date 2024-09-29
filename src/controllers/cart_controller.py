from flask import Blueprint

from init import db
from models.cart import Cart, cart_schema

cart_bp = Blueprint("cart", __name__, url_prefix="/cart")

# /cart - GET - fetch all cart
@cart_bp.route("/")
def get_all_cart():
    stmt = db.select(Cart).order_by(Cart.date.desc())
    cart = db.session.scalars(stmt)
    return cart_schema.dump(cart)

# /cart/<id> - GET - fetch a specific cart
@cart_bp.route("/<int:cart_id>")
def get_a_cart(cart_id):
    stmt = db.select(Cart).filter_by(id=cart_id)
    cart = db.session.scalar(stmt)
    if cart:
        return cart_schema.dump(cart)
    else:
        return {"Error": f"cart with id {cart_id} not found"}, 404
