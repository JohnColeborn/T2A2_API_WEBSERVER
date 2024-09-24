from init import db, ma
from marshmallow import fields
from sqlalchemy.orm import backref

class Cart(db.Model):
    __tablename__ = "cart"

    id = db.Column(db.Integer, primary_key = True)
    cost = db.Column(db.Float, nullable = False)
    date = db.Column(db.Date) #Timestamp on cart Creation

    # foreign keys
    order_id = db.Column(db.Integer, db.ForeignKey("orders.id", ondelete='CASCADE'), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)

    # relationships
    user = db.relationship('User', back_populates='cart')
    orders = db.relationship('Orders', backref=backref("Orders", cascade="all,delete"))

class CartSchema(ma.Schema):
    user = fields.Nested('UserSchema', only = ["id"])  
    orders = fields.Nested('OrdersSchema', exclude = ["id", "cart"])

    class Meta:
        fields = ("id", "cost", "orders", "date", "user")
        ordered = True

cart_schema = CartSchema()
