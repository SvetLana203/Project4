from datetime import datetime
from models.db import db
from sqlalchemy.orm import joinedload

class CartItem(db.Model):
  __tablename__ = "cart_item"

  id = db.Column(db.Integer, primary_key=True)
  cart_id = db.Column(db.Integer, db.ForeignKey('carts.id'))
  item_id = db.Column(db.Integer, db.ForeignKey('items.id'))
  cart = db.relationship("Cart")
  item = db.relationship("Item")

  def __init__(self, cart_id, item_id):
    self.cart_id = cart_id
    self.item_id = item_id

  def json(self):
    return {
      "id": self.id,
      "cart_id": self.cart_id,
      "item_id": self.item_id
    }

  @classmethod
  def find_all(cls):
    query = CartItem.query.options(joinedload(
            'cart')).all()
    response = []
    for item in query:
          response.append({**item.json(), "cart": item.cart.json()})
    return response