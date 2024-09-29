from init import db, ma
from marshmallow import fields

class Ingredients(db.Model):
    __tablename__ = "ingredients"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False)
    quantity = db.Column(db.String(50), nullable = False)

    # foreign keys
    prices_id = db.Column(db.Integer, db.ForeignKey("prices.id"), nullable = False)
    
    # relationships
    orders = db.relationship('Orders', back_populates='ingredients')
    prices = db.relationship('Prices', back_populates='ingredients')
    recipe_ingredients = db.relationship('Recipe_Ingredients', back_populates='ingredients')

class IngredientsSchema(ma.Schema):
    prices = fields.Nested('PricesSchema', only = ["id"])
    orders = fields.Nested('OrdersSchema', only = ["amount"])

    class Meta:
        fields = ("id", "name", "quantity","prices","orders")
        ordered = True

ingredients_schemas = IngredientsSchema(many = True)