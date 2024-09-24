from init import db, ma
from marshmallow import fields

class Orders(db.Model):
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key = True)
    amount = db.Column(db.Float)
    
    # foreign keys
    ingredients_id = db.Column(db.Integer, db.ForeignKey("ingredients.id"), nullable = False)
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipe.id"), nullable = True)
    
    
    # relationships
    recipe = db.relationship('Recipe', foreign_keys=[recipe_id])
    ingredients = db.relationship('Ingredients', foreign_keys=[ingredients_id])
    cart = db.relationship('Cart', back_populates='orders')
    
class OrdersSchema(ma.Schema):
    recipe = fields.Nested('RecipeSchema')
    ingredients = fields.Nested('IngredientsSchema')
    cart = fields.Nested('CartSchema')

    class Meta:
        fields = ("id", "ingredients", "recipe", "cart", "amount")
        ordered = True

orders_schema = OrdersSchema()
orders_schemas = OrdersSchema(many = True)