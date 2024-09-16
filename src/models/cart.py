from init import db, ma
from marshmallow import fields

class Cart(db.Model):
    __tablename__ = "cart"

    id = db.Column(db.Integer, primary_key = True)
    cost = db.Column(db.Float, nullable = False)
    date = db.Column(db.Date) #Timestamp on cart Creation
    order = db.Column(db.Integer, db.ForeignKey("orders.id"), nullable = False)
    user = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)

    user = db.relationship('User', back_populates='cart')
    order = db.relationship('Order', back_populates='cart')

class CartSchema(ma.Schema):
    user = fields.Nested('UserSchema', only = ["id", "name", "email"])  
    order = fields.Nested('OrderSchema')

    class Meta:
        fields = ("id", "cost", "order", "date", "user")
        ordered = True

cart_schema = CartSchema()
