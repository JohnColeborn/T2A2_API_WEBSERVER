from init import db, ma

class Recipe(db.Model):
    __tablename__ = "recipe"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False)
    method = db.Column(db.String(500), nullable = False)

    
class RecipeSchema(ma.Schema):

    class Meta:
        fields = ("id", "name", "method")
        ordered = True

recipe_schema = RecipeSchema()
recipe_schemas = RecipeSchema(Many = True)