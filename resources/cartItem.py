from models.cartItem import CartItem
from models.db import db
from flask_restful import Resource
from flask import request
from sqlalchemy.orm import joinedload

class CartItems(Resource):
  def get(self):
    cartItems = CartItem.find_all()
    return cartItems

  def post(self):
    data = request.get_json()
    params = {}
    for k in data.keys():
      params[k] = data[k]
    cartItem = CartItem(**params)
    cartItem.create()
    return cartItem.json(), 201

class CartItemInfo(Resource):
  def get(self, cart_id):
    cartItems = CartItem.query.filter_by(cart_id=cart_id)
    cart_id = [c.json() for c in cartItems]
    return {**cartItems.json(), "cart_id": cart_id}