from init import db, ma
from marshmallow import fields

class Ingredients(db.Model):
    __tablename__ = "ingredients"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False)
    quantity = db.Column(db.String(50), nullable = False)
    prices_id = db.Column(db.Integer, db.ForeignKey("prices.id"), nullable = False)

    
class IngredientsSchema(ma.Schema):
    prices_id = fields.Nested('PricesSchema')  

    class Meta:
        fields = ("id", "name", "quantity","prices_id")
        ordered = True

ingredients_schema = IngredientsSchema()
ingredients_schemas = IngredientsSchema(Many = True)