from init import db, ma
from marshmallow import fields
from marshmallow.validate import Regexp

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    email = db.Column(db.String, nullable = False, unique = True)
    password = db.Column(db.String, nullable = False)   
     
    cart = db.relationship("Cart", back_populates = "user")
    
class UserSchema(ma.Schema):
    cart = fields.List(fields.Nested('CartSchema', exclude = ["user"]))   

    # Extra Validation
    email = fields.String(required=True, validate = Regexp("^\S+@\S+\.\S+$", error="Invalid email format"))
    
    class Meta:        
        fields = ("id", "name", "email", "password", "cart")

# to handle a single user object
user_schema = UserSchema(exclude=["password"])


# to handle a list of user objects
users_schema = UserSchema(many = True, exclude=["password"])