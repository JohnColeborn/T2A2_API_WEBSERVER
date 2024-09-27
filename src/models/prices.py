from init import db, ma
from marshmallow import fields

class Prices(db.Model):
    __tablename__ = "prices"

    id = db.Column(db.Integer, primary_key = True)
    perweight = db.Column(db.String(50))
    perquantity = db.Column(db.String(50))   
    
    ingredients = db.relationship('Ingredients', cascade='all, delete')

class PricesSchema(ma.Schema):
    ingredients = fields.List(fields.Nested('IngredientsSchema', exclude = ["prices"]))  

    class Meta:
        fields = ("id", "perweight", "perquantity")
        ordered = True

prices_schema = PricesSchema()
