from datetime import date

from flask import Blueprint
from init import db, bcrypt
from models.user import User
from models.cart import Cart
from models.orders import Orders
from models.recipes import Recipe
from models.ingredients import Ingredients
from models.prices import Prices
from models.recipe_ingredients import Recipe_Ingredients

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
            user = users[0],
            orders = []
        ),
        Cart(
            cost = 134.50,           
            date = date.today(),
            user = users[1],
            orders = []
        ),
        Cart(
            cost = 234.50,           
            date = date.today(),
            user = users[0],
            orders = []
        )
    ]

    db.session.add_all(cart)   

    orders = [
        Orders(
            amount = 5
        ),
         Orders(
            amount = 15
        ),
         Orders(
            amount = 25
        )
    ]

    db.session.add_all(orders)

    recipes = [
        Recipe(
            name = "Choc Chip Bikky",
            method = "Take dough, apply yum, cook well, enjoy"
        ),
           Recipe(
            name = "Peanut Bikky",
            method = "Take dough, apply nuts, cook well, enjoy"
        ),
           Recipe(
            name = "Raisin Bikky",
            method = "Take dough, apply raisins, cook well, enjoy"
        )
    ]

    db.session.add_all(recipes)

    ingredients = [
        Ingredients(
            name = "flour",
            quantity = "1 KG", 
            prices = 1           
        ),
        Ingredients(
            name = "sugar",
            quantity = "2 KG",
            prices = 2
        ),
        Ingredients(
            name = "nuts",
            quantity = "100 gm",
            prices = 3
        ),
        Ingredients(
            name = "raisins",
            quantity = "150 gm",
            prices = 4
        ),
        Ingredients(
            name = "chocolate",
            quantity = "500 gm",
            prices = 5
        )
    ]

    db.session.add_all(ingredients)

    prices = [
        Prices(
            perweight = "$1.50 / KG",
            perquantity = "$2 / Each",
            id = 1
        ),
            Prices(
            perweight = "$13.50 / KG",
            id = 2
        ),
            Prices(
            perquantity = "$10 / Each",
            id = 3
        ),
            Prices(
            perweight = "$11.50 / KG",
            perquantity = "$1 / Each",
            id = 4
        ),
            Prices(
            perweight = "$19.50 / KG",
            perquantity = "$3 / Each",
            id = 5
        ),
    ]

    db.session.add_all(prices)

    recipe_ingredients = [
        Recipe_Ingredients(
            use_quantity = "4 Eggs"
        ),
        Recipe_Ingredients(
            use_quantity = "100gm Flour"
        ),
        Recipe_Ingredients(
            use_quantity = "200gm Sugar"
        ),
        Recipe_Ingredients(
            use_quantity = "400gm Chocolate"
        ),
        Recipe_Ingredients(
            use_quantity = "200gm Nuts"
        ),
        Recipe_Ingredients(
            use_quantity = "100gm Raisins"
        )
    ]
    
    db.session.add_all(recipe_ingredients)

    db.session.commit()

    print("User Tables Seeded!")

@db_commands.cli.command("drop")
def drop_tables():
    db.drop_all()
    print("Tables Dropped.")