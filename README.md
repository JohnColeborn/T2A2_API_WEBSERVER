# Ecommerce API
### Github: https://github.com/JohnColeborn/T2A2_API_WEBSERVER

# App Purpose
This app is designed to aid functionality on an ecommerce site by allowing tables to populate each other and output to a final table viewable by a user. In this case the 'Cart'. The user is able to register, login, and securely create, modify, and delete their orders. They are also able to view ingredients and prices.

Data supplied by the host integrates tables such as 'prices', 'ingredients' and 'orders' and present them to the user as a collected table 'cart'.

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
Database is built using 5 models, (cart, ingredients, orders, prices, user).

Modified ERM to show relations:

![ERDscreenshot](/docs/finalEntity.png)


# Post-Code commenced explanation of relations
Tasks are allocated in the following format:
    
Register user, through the use of 'POST', data is supplied by the user and passed to the server in the body of the request.  Once registered the user can > Login

![insomniaregister](/docs/register.png)


Login user again requires data from the user, also using 'POST', and will provide the client with a session token to prove they are the authorised user.

![insomnialogin](/docs/login.png)

User will then access the cart, through a 'GET' call, and will then be able to see the cost, the date created and confirmation of current user.

![cart](/docs/cart.png)


Orders are also accessed through a 'GET' query, this table is the enabler that allows the user to see the current state of ordering from ingredients

![orders](/docs/orders.png)

Orders shows :
- Order ID
- Ingredients:
    - Name
    - Quantity
    - Prices
- Amount Ordered

The user is able to delete, create, and modify the orders table through 'DELETE', 'POST' and 'PUT' / 'PATCH', to perform these actions requires JSON inputs in the body, as well as JWT authentication (taken from the login user 'POST').

Here we see 'DELETE', it does not need body data, but it does require the added ID number of the order (/1 in this example) to delete in the link.

![delete](/docs/deleteOrder.png)

Likewise 'PATCH' can be used to modify an existing order, requiring order ID in the link, authentication through JWT, and data in the body.

![modify](/docs/modOrder.png)

To create a new order the user is required to fill the body data with the ingredient id (found in ingredients table), and the amount, it also requires authentication with JWT

![create](/docs/createOrder.png)

Ingredients is pulled through 'GET' to populate Orders
    
![ingredients](/docs/ingredients.png)

Ingredients shows:
- Ingredient ID
- Ingredient Name
- Quantity unit per ingredient
- Prices

Prices is pulled with 'GET' to populate Ingredients

![prices](/docs/prices.png)

Prices: Show Value Per Weight of Ingredient,

Prices: Show Value Per Quantity of Ingredient.

# Best bit of the entire experience:
![quintessence](/docs/finalTrello.png)    