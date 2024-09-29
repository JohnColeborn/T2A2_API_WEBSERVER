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

