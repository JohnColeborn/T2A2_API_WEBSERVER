from datetime import date

from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from init import db
from models.orders import Orders, order_schema,orders_schema

orders_bp = Blueprint("orders", __name__, url_prefix="/orders")

# /orders - GET - fetch all orders
@orders_bp.route("/")
def get_all_orders():
    stmt = db.select(Orders)
    orders = db.session.scalars(stmt)
    return orders_schema.dump(orders)

# /orders - POST - create a new orders
@orders_bp.route("/", methods = ["POST"])
@jwt_required()
def create_order():
    # get data from body of request
    body_data = order_schema.load(request.get_json())
    # create new orders model instance
    orders = Orders(
        # Fetch ingredients_id from body
        ingredients_id=body_data.get("ingredients_id"),  
        amount=body_data.get("amount")        
    )
    # add and commit to db
    db.session.add(orders)
    db.session.commit()
    # response message
    return order_schema.dump(orders)


# /orders/<id> - DELETE - delete a orders
@orders_bp.route("/<int:orders_id>", methods = ["DELETE"])
@jwt_required()
def delete_orders(orders_id):
    # fetch the orders from database
    stmt = db.select(Orders).filter_by(id = orders_id)
    orders = db.session.scalar(stmt)
    # if orders exists
    if orders:
        # delete orders
        db.session.delete(orders)
        db.session.commit()
        return {"message": f"orders {orders.id} deleted succesfully"}
    # else
    else:
        # return error
        return {"error": f"orders with id {orders_id} not found"}, 404

# /orders/<id> - PUT, PATCH - edit a orders
@orders_bp.route("/<int:orders_id>", methods = ["PUT", "PATCH"])
@jwt_required()
def update_orders(orders_id):
    # get the info from the body of the request
    body_data = order_schema.load(request.get_json(), partial = True)
    # get the orders from the database
    stmt = db.select(Orders).filter_by(id = orders_id)
    orders = db.session.scalar(stmt)
    # if the orders exists 
    if orders:
    # update the fields as required 
        orders.ingredients = body_data.get("ingredients") or orders.ingredients
        orders.amount = body_data.get("amount") or orders.amount
    # commit to DB 
        db.session.commit()
    # return message 
        return order_schema.dump(orders)
    # else 
    else:        
    # return error message
        return {"error": f"order with id {orders_id} not found"}, 404