from init import db, ma
from marshmallow import fields

class Recipe_Ingredients(db.Model):
    __tablename__ = "recipe_ingredients"

    id = db.Column(db.Integer, primary_key = True)
    ingredients_id = db.Column(db.Integer, db.ForeignKey("ingredients.id"), nullable = False)
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipe.id"), nullable = False)
    quantity = db.Column(db.String)

    recipe = db.relationship('Recipe', foreign_keys=[recipe_id])
    ingredients = db.relationship('Ingredients', foreign_keys = [ingredients_id])
    
class Recipe_IngredientsSchema(ma.Schema):
    recipe = fields.Nested('RecipeSchema')
    ingredients = fields.Nested('IngredientsSchema')  

    class Meta:
        fields = ("id", "ingredients", "recipe")
        ordered = True

recipe_ingredients_schema = Recipe_IngredientsSchema()
recipe_ingredients_schemas = Recipe_IngredientsSchema(many = True)