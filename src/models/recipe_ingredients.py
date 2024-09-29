from init import db, ma
from marshmallow import fields

class Recipe_Ingredients(db.Model):
    __tablename__ = "recipe_ingredients"

    id = db.Column(db.Integer, primary_key = True)
    use_quantity = db.Column(db.String)

    # foreign keys
    ingredients_id = db.Column(db.Integer, db.ForeignKey("ingredients.id"), nullable = False)
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipe.id"), nullable = False)
    
    # relations
    recipe = db.relationship('Recipe', back_populates='recipe_ingredients')
    ingredients = db.relationship('Ingredients', back_populates='recipe_ingredients')
    
class Recipe_IngredientsSchema(ma.Schema):
    recipe = fields.Nested('RecipeSchema', only = ["id","name"])
    ingredients = fields.Nested('IngredientsSchema', only = ["id", "name"])

    class Meta:
        fields = ("id", "ingredients", "recipe","use_quantity")
        ordered = True

recipe_ingredients_schema = Recipe_IngredientsSchema(many = True)