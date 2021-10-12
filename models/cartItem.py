from datetime import datetime
from models.db import db
from sqlalchemy.orm import joinedload

class CartItem(db.Model):
  __tablename__ = "cart_item"

  id = db.Column(db.Integer, primary_key=True)
  cart_id = db.Column(db.Integer, db.ForeignKey('carts.id'))
  item_id = db.Column(db.Integer, db.ForeignKey('items.id'))
  cart = db.relationship("Cart", backref=db.backref('carts', lazy=True))
  item = db.relationship("Item", backref=db.backref('cart_items', lazy=True))

  def __init__(self, cart_id, item_id):
    self.cart_id = cart_id
    self.item_id = item_id

  def json(self):
    return {
      "id": self.id,
      "cart_id": self.cart_id,
      "item_id": self.item_id
    }
  def create(self):
    db.session.add(self)
    db.session.commit()
    return self

  @classmethod
  def find_all(cls):
    query = CartItem.query.options(joinedload(
            'cart')).all()
    response = []
    for item in query:
          response.append({**item.json(), "cart": item.cart.json()})
    return response