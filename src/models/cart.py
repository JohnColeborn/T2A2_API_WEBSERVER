from init import db, ma
from marshmallow import fields, validates
from marshmallow.validate import Length, And, Regexp, OneOf
from marshmallow.exceptions import ValidationError

class Cart(db.Model):
    __tablename__ = "cart"

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String, nullable = False)
    description = db.Column(db.String)
    status = db.Column(db.String)
    priority = db.Column(db.String)
    date = db.Column(db.Date) #Timestamp on cart Creation

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)

    user = db.relationship('User', back_populates='cart')    
class CartSchema(ma.Schema):
    user = fields.Nested('UserSchema', only = ["id", "name", "email"])  

    class Meta:
        fields = ("id", "title", "description", "status", "priority", "date", "user")
        ordered = True

cart_schema = CartSchema()
