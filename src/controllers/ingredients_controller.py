from flask import Blueprint

from init import db
from models.ingredients import Ingredients, ingredients_schema

ingredients_bp = Blueprint("ingredients", __name__, url_prefix="/ingredients")

# /ingredients - GET - fetch all ingredients
@ingredients_bp.route("/")
def get_all_ingredients():
    stmt = db.select(Ingredients)
    ingredients = db.session.scalars(stmt)
    return ingredients_schema.dump(ingredients)

# /ingredients/<id> - GET - fetch a specific ingredients
@ingredients_bp.route("/<int:ingredients_id>")
def get_a_ingredients(ingredients_id):
    stmt = db.select(Ingredients).filter_by(id=ingredients_id)
    ingredients = db.session.scalar(stmt)
    if ingredients:
        return ingredients_schema.dump(ingredients)
    else:
        return {"Error": f"ingredients with id {ingredients_id} not found"}, 404
