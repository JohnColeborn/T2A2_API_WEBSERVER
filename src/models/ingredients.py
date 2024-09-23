from init import db, ma
from marshmallow import fields

class Ingredients(db.Model):
    __tablename__ = "ingredients"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False)
    quantity = db.Column(db.String(50), nullable = False)
    prices_id = db.Column(db.Integer, db.ForeignKey("prices.id"), nullable = False)
 
    orders = db.relationship('Orders', back_populates='ingredients')
    prices = db.relationship('Prices')
    recipe_ingredients = db.relationship('Recipe_Ingredients')

class IngredientsSchema(ma.Schema):
    prices_id = fields.Nested('PricesSchema')  
    orders = fields.Nested('OrdersSchema', only = ["amount"])

    class Meta:
        fields = ("id", "name", "quantity","prices","orders")
        ordered = True

ingredients_schema = IngredientsSchema()
ingredients_schemas = IngredientsSchema(many = True)