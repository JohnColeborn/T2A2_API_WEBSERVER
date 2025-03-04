from init import db, ma
from marshmallow import fields

class Prices(db.Model):
    __tablename__ = "prices"

    id = db.Column(db.Integer, primary_key = True)
    perweight = db.Column(db.String(50), nullable = True)
    perquantity = db.Column(db.String(50), nullable = True)   
    
    ingredients = db.relationship('Ingredients',back_populates='prices', cascade='all, delete')

class PricesSchema(ma.Schema):
    ingredients = fields.Nested('IngredientsSchema', exclude = ["prices"])

    class Meta:
        fields = ("id", "perweight", "perquantity")
        ordered = True



prices_schema = PricesSchema(many = True)
