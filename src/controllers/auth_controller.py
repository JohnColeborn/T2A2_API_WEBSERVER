from flask import Blueprint, request
from models.user import User, user_schema, UserSchema
from init import bcrypt, db
from sqlalchemy.exc import IntegrityError
from psycopg2 import errorcodes
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from datetime import timedelta

auth_bp = Blueprint("auth", __name__, url_prefix = "/auth")

@auth_bp.route("/register", methods = ["POST"])
def register_user():
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


@auth_bp.route("/login", methods = ["POST"])
def login_user():
    # Get datas from body of request
    body_data = request.get_json()
    # Find user in DB with email address
    stmt = db.select(User).filter_by(email = body_data.get("email"))
    user = db.session.scalar(stmt)
    # IF user exists and pw is correct
    if user and bcrypt.check_password_hash(user.password, body_data.get("password")):
        # create JWT
        token = create_access_token(identity = str(user.id), expires_delta = timedelta(days = 1))
        # return respons
        return {"email": user.email, "is_admin": user.is_admin, "token": token}
    # Else
    else:
        # respond with error
        return {"error": "Invalid user name or password"}, 401
    

# /auth/users/user_id
@auth_bp.route("/users/", methods=["PUT", "PATCH"])
@jwt_required()
def update_user():
    # get the fields from the body of the request
    body_data = UserSchema().load(request.get_json(), partial=True)
    password = body_data.get("password")
    # fetch the user from the db
    stmt = db.select(User).filter_by(id=get_jwt_identity())
    user = db.session.scalar(stmt)
    # if exists:
    if user:
    #     update the fields as required 
        user.name = body_data.get("name") or user.name
        if password:
            user.password = bcrypt.generate_password_hash(password).decodde("utf-8")
    #     commit to the db
        db.session.commit()
    #     return a response
        return user_schema.dump(user)
    # else:
    else:
        # return error response
        return {"error": "User does not exist"}