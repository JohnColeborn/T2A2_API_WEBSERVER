from datetime import date

from flask import Blueprint
from init import db, bcrypt
from models.user import User
from models.cart import Cart
# from models.comment import Comment

db_commands = Blueprint("db", __name__)

@db_commands.cli.command("create")
def create_tables():
    db.create_all()
    print("Tables Created")

@db_commands.cli.command("seed")
def seed_tables():
    # Create a list of user instances
    users = [
        User(
            name = "Admin",
            email = "admin@email.com",
            password = bcrypt.generate_password_hash("123456").decode("utf-8"),
        ), 
        User(
            name = "User A",
            email = "usera@email.com",
            password = bcrypt.generate_password_hash("123456").decode("utf-8")
        )
    ]

    db.session.add_all(users)

    cart = [
        Cart(        
            cost = 34.50,           
            date = date.today(),
            user = users[0]
        ),
        Cart(
            cost = 134.50,           
            date = date.today(),
            user = users[1]
        ),
        Cart(
            cost = 234.50,           
            date = date.today(),
            user = users[0]
        )
    ]

    db.session.add_all(cart)   

    db.session.commit()

    print("User Tables Seeded!")

@db_commands.cli.command("drop")
def drop_tables():
    db.drop_all()
    print("Tables Dropped.")