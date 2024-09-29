import os
from flask import Flask
from marshmallow.exceptions import ValidationError

from init import db, ma, bcrypt, jwt
from controllers.cli_controllers import db_commands
from controllers.auth_controller import auth_bp
from controllers.cart_controller import cart_bp
from controllers.price_controller import prices_bp
from controllers.ingredients_controller import ingredients_bp
from controllers.recipe_ingredients_controller import recipe_ingredients_bp
from controllers.orders_controller import orders_bp
from controllers.recipe_controller import recipe_bp

def create_app():
    app = Flask(__name__)
    app.json.sort_keys = False
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
    app.config["JWT_SECRET_KEY"] = os.environ.get("JWT_SECRET_KEY")

    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    @app.errorhandler(ValidationError)
    def validation_error(err):
        return {"error": err.messages}, 400

    app.register_blueprint(db_commands)
    app.register_blueprint(auth_bp)
    app.register_blueprint(cart_bp)
    app.register_blueprint(prices_bp)
    app.register_blueprint(ingredients_bp)
    app.register_blueprint(recipe_ingredients_bp)
    app.register_blueprint(orders_bp)
    app.register_blueprint(recipe_bp)
    
    return app