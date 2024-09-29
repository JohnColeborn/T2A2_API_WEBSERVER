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
        users = User(
            name = body_data.get("name"),
            email = body_data.get("email")
        )
        # HASH the password
        password = body_data.get("password")
        if password:
            users.password = bcrypt.generate_password_hash(password).decode("utf-8")
        # ADD and COMMIT to the DB
        db.session.add(users)
        db.session.commit()
        # Return Acknowledgement
        return user_schema.dump(users), 201
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
    users = db.session.scalar(stmt)
    # IF user exists and pw is correct
    if users and bcrypt.check_password_hash(users.password, body_data.get("password")):
        # create JWT
        token = create_access_token(identity = str(users.id), expires_delta = timedelta(days = 1))
        # return respons
        return {"email": users.email, "token": token}
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
    users = db.session.scalar(stmt)
    # if exists:
    if users:
    #     update the fields as required 
        users.name = body_data.get("name") or users.name
        if password:
            users.password = bcrypt.generate_password_hash(password).decodde("utf-8")
    #     commit to the db
        db.session.commit()
    #     return a response
        return user_schema.dump(users)
    # else:
    else:
        # return error response
        return {"error": "User does not exist"}