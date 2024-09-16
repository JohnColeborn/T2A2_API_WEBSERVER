from init import db, ma
from marshmallow import fields

class Recipe_Ingredients(db.Model):
    __tablename__ = "recipe_ingredients"

    id = db.Column(db.Integer, primary_key = True)
    ingredients = db.Column(db.Integer, db.ForeignKey("ingredients.id"), nullable = False)
    recipe = db.Column(db.Integer, db.ForeignKey("recipe.id"), nullable = False)

    
class Recipe_IngredientsSchema(ma.Schema):
    recipe = fields.Nested('RecipeSchema')
    ingredients = fields.Nested('IngredientsSchema')  

    class Meta:
        fields = ("id", "ingredients", "recipe")
        ordered = True

recipe_ingredients_schema = Recipe_IngredientsSchema()
recipe_ingredients_schemas = Recipe_IngredientsSchema(Many = True)