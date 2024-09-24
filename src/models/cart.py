from init import db, ma
from marshmallow import fields

class Cart(db.Model):
    __tablename__ = "cart"

    id = db.Column(db.Integer, primary_key = True)
    cost = db.Column(db.Float, nullable = False)
    date = db.Column(db.Date) #Timestamp on cart Creation

    # foreign keys
    order_id = db.Column(db.Integer, db.ForeignKey("orders.id"), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)

    # relationships
    user = db.relationship('User', foreign_keys=[user_id])
    orders = db.relationship('Orders', foreign_keys=[order_id], back_populates='cart')

class CartSchema(ma.Schema):
    user = fields.Nested('UserSchema', only = ["id"])  
    orders = fields.Nested('OrdersSchema', only = ["id", "amount"])

    class Meta:
        fields = ("id", "cost", "orders", "date", "user")
        ordered = True

cart_schema = CartSchema()
