from flask import Blueprint

from init import db
from models.prices import Prices, prices_schema

prices_bp = Blueprint("prices", __name__, url_prefix="/prices")

# /prices - GET - fetch all prices
@prices_bp.route("/")
def get_all_prices():
    stmt = db.select(Prices)
    prices = db.session.scalars(stmt)
    return prices_schema.dump(prices)

# /prices/<id> - GET - fetch a specific prices
@prices_bp.route("/<int:prices_id>")
def get_a_prices(prices_id):
    stmt = db.select(Prices).filter_by(id=prices_id)
    prices = db.session.scalar(stmt)
    if prices:
        return prices_schema.dump(prices)
    else:
        return {"Error": f"prices with id {prices_id} not found"}, 404
