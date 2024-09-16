from init import db, ma
from marshmallow import fields

class Prices(db.Model):
    __tablename__ = "prices"

    id = db.Column(db.Integer, primary_key = True)
    perweight = db.Column(db.String(50))
    perquantity = db.Column(db.String(50))   
    
class PricesSchema(ma.Schema):
    prices_id = fields.Nested('PricesSchema')  

    class Meta:
        fields = ("id", "perweight", "perquantity")
        ordered = True

prices_schema = PricesSchema()
