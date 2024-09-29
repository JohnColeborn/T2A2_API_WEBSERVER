from flask import Blueprint

from init import db
from models.recipe_ingredients import Recipe_Ingredients, recipe_ingredients_schema

recipe_ingredients_bp = Blueprint("recipe_ingredients", __name__, url_prefix="/recipe_ingredients")

# /recipe_ingredients - GET - fetch all recipe_ingredients
@recipe_ingredients_bp.route("/")
def get_all_recipe_ingredients():
    stmt = db.select(Recipe_Ingredients)
    recipe_ingredients = db.session.scalars(stmt)
    return recipe_ingredients_schema.dump(recipe_ingredients)

