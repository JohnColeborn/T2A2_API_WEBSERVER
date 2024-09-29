from datetime import date

from flask import Blueprint
from init import db, bcrypt
from models.user import User
from models.cart import Cart
from models.orders import Orders
from models.ingredients import Ingredients
from models.prices import Prices


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
            password = bcrypt.generate_password_hash("123456").decode("utf-8")            
        ), 
        User(
            name = "User A",
            email = "usera@email.com",
            password = bcrypt.generate_password_hash("123456").decode("utf-8")
        )
    ]

    db.session.add_all(users)

    prices = [
        Prices(
            perweight = "$1.50 / KG",
            perquantity = "$2 / Each"
        ),
            Prices(
            perweight = "$13.50 / KG"
        ),
            Prices(
            perquantity = "$10 / Each"
        ),
            Prices(
            perweight = "$11.50 / KG",
            perquantity = "$1 / Each"
        ),
            Prices(
            perweight = "$19.50 / KG",
            perquantity = "$3 / Each"
        ),
    ]

    db.session.add_all(prices)

    ingredients = [
        Ingredients(
            name = "flour",
            quantity = "1 KG",             
            prices = prices[0]          
        ),
        Ingredients(
            name = "sugar",
            quantity = "2 KG",
            prices = prices[1]
        ),
        Ingredients(
            name = "nuts",
            quantity = "100 gm",
            prices = prices[2]
        ),
        Ingredients(
            name = "raisins",
            quantity = "150 gm",
            prices = prices[3]
        ),
        Ingredients(
            name = "chocolate",
            quantity = "500 gm",
            prices = prices[4]
        )
    ]

    db.session.add_all(ingredients) 

    orders = [
        Orders(
            amount = 5,
            ingredients = ingredients[0]                       
        ),
         Orders(
            amount = 15,
            ingredients = ingredients[1]                              
        ),
         Orders(
            amount = 25,
            ingredients = ingredients[2]                               
        )
    ]

    db.session.add_all(orders)    

    cart = [
        Cart(        
            cost = 34.50,           
            date = date.today(),    
            users = users[0],        
            orders = []
        ),
        Cart(
            cost = 134.50,           
            date = date.today(),
            users = users[1],           
            orders = []
        ),
        Cart(
            cost = 234.50,           
            date = date.today(),
            users = users[0],          
            orders = []
        )
    ]

    db.session.add_all(cart)    

    db.session.commit()

    print("Tables Seeded!")

@db_commands.cli.command("drop")
def drop_tables():
    db.drop_all()
    print("Tables Dropped.")