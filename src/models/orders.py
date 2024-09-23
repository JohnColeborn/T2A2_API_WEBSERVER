from init import db, ma
from marshmallow import fields

class Orders(db.Model):
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key = True)

    ingredients_id = db.Column(db.Integer, db.ForeignKey("ingredients.id"), nullable = False)
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipe.id"), nullable = False)
    cart_id = db.Column(db.Integer, db.ForeignKey("cart.id"), nullable = False)

    amount = db.Column(db.Float)

    recipe = db.relationship('Recipe', foreign_keys=[recipe_id])
    ingredients = db.relationship('Ingredients', foreign_keys=[ingredients_id])
    cart = db.relationship('Cart', foreign_keys=[cart_id])
    
class OrdersSchema(ma.Schema):
    recipe = fields.Nested('RecipeSchema')
    ingredients = fields.Nested('IngredientsSchema')
    

    class Meta:
        fields = ("id", "ingredients", "recipe", "cart", "amount")
        ordered = True

orders_schema = OrdersSchema()
orders_schemas = OrdersSchema(many = True)