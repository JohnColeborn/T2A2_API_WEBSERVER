from flask import Blueprint

from init import db
from models.recipes import Recipe, recipe_schema

recipe_bp = Blueprint("recipe", __name__, url_prefix="/recipe")

# /recipe - GET - fetch all recipe
@recipe_bp.route("/")
def get_all_recipe():
    stmt = db.select(Recipe)
    recipe = db.session.scalars(stmt)
    return recipe_schema.dump(recipe)

