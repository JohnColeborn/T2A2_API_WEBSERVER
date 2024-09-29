from init import db, ma
from marshmallow import fields

class Orders(db.Model):
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key = True)
    amount = db.Column(db.Float)
    
    # foreign keys
    ingredients_id = db.Column(db.Integer, db.ForeignKey("ingredients.id"), nullable = False)
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipe.id"), nullable = True)
    cart_id = db.Column(db.Integer, db.ForeignKey("cart.id"),nullable = True)
    
    # relationships
    recipe = db.relationship('Recipe', back_populates='orders')
    ingredients = db.relationship('Ingredients', back_populates='orders')
    cart = db.relationship('Cart', back_populates='orders', cascade="all,delete")
    
class OrdersSchema(ma.Schema):
    recipe = fields.Nested('RecipeSchema', only=["name"])
    ingredients = fields.Nested('IngredientsSchema', only=["name"])
    cart = fields.Nested('CartSchema', exclude=["orders"])

    class Meta:
        fields = ("id", "ingredients", "recipe", "cart", "amount")
        ordered = True

orders_schema = OrdersSchema(many = True)