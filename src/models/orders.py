from init import db, ma
from marshmallow import fields

class Orders(db.Model):
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key = True)
    amount = db.Column(db.Float)
    
    # foreign keys
    ingredients_id = db.Column(db.Integer, db.ForeignKey("ingredients.id"), nullable = False)
    cart_id = db.Column(db.Integer, db.ForeignKey("cart.id"),nullable = True)
    
    # relationships 
    ingredients = db.relationship('Ingredients', back_populates='orders')
    cart = db.relationship('Cart', back_populates='orders', cascade="all,delete")
    
class OrdersSchema(ma.Schema): 
    ingredients_id = fields.Integer(required=True)  # Explicitly declare ingredients_id as Integer
    ingredients = fields.Nested('IngredientsSchema', only=["name", "quantity", "prices"])
    

    class Meta:
        fields = ("id","ingredients_id", "ingredients", "amount")
        ordered = True

# For a single order
order_schema = OrdersSchema()

# For multiple orders
orders_schema = OrdersSchema(many=True)