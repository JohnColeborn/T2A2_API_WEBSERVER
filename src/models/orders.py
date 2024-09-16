from init import db, ma
from marshmallow import fields

class Orders(db.Model):
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key = True)
    ingredients = db.Column(db.Integer, db.ForeignKey("ingredients.id"), nullable = False)
    recipe = db.Column(db.Integer, db.ForeignKey("recipe.id"), nullable = False)
    cart = db.Column(db.Integer, db.ForeignKey("cart.id"), nullable = False)
    amount = db.Column(db.Float)
    
class OrdersSchema(ma.Schema):
    recipe = fields.Nested('RecipeSchema')
    ingredients = fields.Nested('IngredientsSchema')


    class Meta:
        fields = ("id", "ingredients", "recipe", "cart", "amount")
        ordered = True

orders_schema = OrdersSchema()
orders_schemas = OrdersSchema(Many = True)