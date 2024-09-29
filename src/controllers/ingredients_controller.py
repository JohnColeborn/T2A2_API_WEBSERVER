from flask import Blueprint

from init import db
from models.ingredients import Ingredients, ingredients_schemas

ingredients_bp = Blueprint("ingredients", __name__, url_prefix="/ingredients")

# /ingredients - GET - fetch all ingredients
@ingredients_bp.route("/")
def get_all_ingredients():
    stmt = db.select(Ingredients)
    ingredients = db.session.scalars(stmt)
    return ingredients_schemas.dump(ingredients)
