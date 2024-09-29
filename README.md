# Ecommerce API
### Github: https://github.com/JohnColeborn/T2A2_API_WEBSERVER

# App Purpose
This app is designed to aid functionality on an ecommerce site by allowing users to browse products, add them to cart, and remove them from cart. 

It does this through the use of multiple features based predominantly around 'cart', 'recipes', and 'ingredients'.

## Initialised Draft Concept
This is done utilising Trello and DrawIO:

![trelloscreenshot](/docs/trelloSS.png)
***
![ERDscreenshot](/docs/entity(1).png)
***
This was then reviewed and revised, and ERD was updated accordingly through a series of revisions bringing us to this 'final' initial ERD

![ERDSSrevised6](/docs/entity(8).png)
# Pre-Code explanation of relations.
Tasks are allocated in the following format:
    
    User: Register user,
    User: Login,
    User: Access Cart,

    Cart: Show Date Created,
    Cart: Show Total Cost,
    Cart: Access Orders,

    Orders: Show Amount Ordered,
    Orders: Access Recipes,
    Orders: Access Ingredients,
    Orders: Access Cart,

    Recipes: Show Name of Recipe,
    Recipes: Show Name of Method,

    Recipe_Ingredients: Show Quantity of Ingredients Used in Recipe,
    Recipe_Ingredients: Access Ingredients,
    Recipe_Ingredients: Access Recipes,

    Ingredients: Show Name of Ingredient,
    Ingredients: Show Base Quantiy of Ingredient,
    Ingredients: Access Prices,

    Prices: Show Value Per Weight of Ingredient,
    Prices: Show Value Per Quantity of Ingredient.
***
![UpdatedTrelloSS](/docs/trelloSS1.png)
***

## Services and Dependencies - 
Flask - A Python based micro web framework

SQLAlchemy - An object relational mapper for database interactions

Psycopg - A PostgreSQL adaptor for Python

Bcrypt - A cipher based password hashing function

JWT Manager - Javascript library for storing and retrieving JWT(JSON Web Tokens)

Marshmallow - An integration layer for Flask to define output schemas based on classes

# Database Pro/Con
Using SQL on a PostgreSQL through Flask and Psycopg make this a great choice in regard to functionality, accessibility, and simplicity. 
However it is a local database and will not ship with the API.

# ORM in Detail
SQLAlchemy is used in this project, and contains many features some of which include:
-   The ability to swap out generated SQL with hand-optimized statements,
-   Supports the widest variety of database and architectural designs as reasonably possible.  
-   Organises pending insert/update/delete operations into queues and flushes them all in one batch.
-   Allows SQL clauses to be built via Python functions and expressions. 

The purpose of SQLAlchemy is to facilitate communication between Python programs and databases (in our case between Flask and PostgreSQL).

The functionalities used include:
-   Translating the classes in our models to tables in our database.
-   Managing the connections between tables.
-   Manipulating the data on the database through python commands.


# Build Database!
Database is built using 7 models, (cart, ingredients, orders, prices, recipe_ingredients, recipes, user).

Modified ERM to show relations:

![ERDscreenshot](/docs/entity(11).png)


# Post-Code commenced explanation of relations
Tasks are allocated in the following format:
    
 User: Register user, Once registered the user can > Login

![insomniaregister](/docs/register.png)


User: Login, Once logged in the user can > Access Cart
User: Access Cart, After accessing the Cart the user will be able to see the current order, the ingredients available, the recipes available, and the pricing.

Cart: Show Date Created, The cart time stamps to show when it was created
Cart: Show Total Cost, It will show the total cost of the current order placed in it by accessing > Orders
Cart: Access Orders, This is the enabler that allows the user to see the current state of ordering from ingredients and recipes.

    Orders: Show Amount Ordered,
    Orders: Access Recipes,
    Orders: Access Ingredients,
    Orders: Access Cart,

    Recipes: Show Name of Recipe,
    Recipes: Show Name of Method,

    Recipe_Ingredients: Show Quantity of Ingredients Used in Recipe,
    Recipe_Ingredients: Access Ingredients,
    Recipe_Ingredients: Access Recipes,

    Ingredients: Show Name of Ingredient,
    Ingredients: Show Base Quantiy of Ingredient,
    Ingredients: Access Prices,

    Prices: Show Value Per Weight of Ingredient,
    Prices: Show Value Per Quantity of Ingredient.