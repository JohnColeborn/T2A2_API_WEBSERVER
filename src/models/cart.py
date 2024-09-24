from init import db, ma
from marshmallow import fields

class Cart(db.Model):
    __tablename__ = "cart"

    id = db.Column(db.Integer, primary_key = True)
    cost = db.Column(db.Float, nullable = False)
    date = db.Column(db.Date) #Timestamp on cart Creation

    # foreign keys
    order_id = db.Column(db.Integer, db.ForeignKey("orders.id"), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable = False)

    # relationships
    user = db.relationship('User', back_populates='cart')
    orders = db.relationship('Orders', back_populates='cart', cascade="all,delete")

class CartSchema(ma.Schema):
    user = fields.List(fields.Nested('UserSchema', exclude = ["password", "cart"]))
    orders = fields.List(fields.Nested('OrdersSchema', exclude = ["cart"]))

    class Meta:
        fields = ("id", "cost", "date", "user", "orders")
        ordered = True

cart_schema = CartSchema()
