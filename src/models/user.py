from init import db, ma
from marshmallow import fields
from marshmallow.validate import Regexp

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = True)
    email = db.Column(db.String, nullable = False, unique = True)
    password = db.Column(db.String, nullable = False)
     

    cart = db.relationship("Cart", back_populates = "users")
    
class UserSchema(ma.Schema):
    cart = fields.List(fields.Nested('CartSchema', exclude = ["users"]))   

    # Extra Validation
    email = fields.String(required=True, validate = Regexp("^\S+@\S+\.\S+$", error="Invalid email format"))
    
    class Meta:        
        fields = ("id", "name", "email", "password", "cart")

# to handle a single user object
user_schema = UserSchema(exclude=["password"])


