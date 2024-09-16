from flask import Blueprint, request
from models.user import User, user_schema, UserSchema
from init import bcrypt, db
from sqlalchemy.exc import IntegrityError
from psycopg2 import errorcodes
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from datetime import timedelta

cart_bp = Blueprint("cart", __name__, url_prefix = "/cart")

@cart_bp.route("/register", methods = ["GET"])
@jwt_required()
def get_cart():
    
    try:
        # GET the data from the body of the request
        body_data = UserSchema().load(request.get_json())
        # Create an instance of the USER model
        user = User(
            name = body_data.get("name"),
            email = body_data.get("email")
        )
        # HASH the password
        password = body_data.get("password")
        if password:
            user.password = bcrypt.generate_password_hash(password).decode("utf-8")
        # ADD and COMMIT to the DB
        db.session.add(user)
        db.session.commit()
        # Return Acknowledgement
        return user_schema.dump(user), 201
    except IntegrityError as err:
        if err.orig.pgcode == errorcodes.NOT_NULL_VIOLATION:
            return {"Error": f"{err.orig.diag.column_name} is Required"}, 400
        if err.orig.pgcode == errorcodes.UNIQUE_VIOLATION:
            return {"Error": "Email Address already Used"}, 400


