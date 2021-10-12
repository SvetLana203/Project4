from datetime import datetime

from sqlalchemy.orm import joinedload
from models.db import db

class Cart(db.Model):
  __tablename__ = "carts"

  id = db.Column(db.Integer, primary_key=True)
  created_at = db.Column(db.DateTime, default=str(
        datetime.utcnow()), nullable=False)
  updated_at = db.Column(db.DateTime, default=datetime.utcnow(
    ), nullable=False, onupdate=datetime.now())
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  
  user = db.relationship("User", backref=db.backref('cart_users', lazy=True))
  def __init__(self, user_id):
    self.user_id = user_id

  def json(self):
    return {
      "id": self.id,
      "created_at": str(self.created_at),
      "updated_at": str(self.updated_at)
    }

  def create(self):
    db.session.add(self)
    db.session.commit()
    return self

  @classmethod
  def find_by_id(cls, user_id):
    cart = Cart.query.filter_by(user_id=user_id)
    return cart
  
  @classmethod
  def find_all(cls):
    query = Cart.query.options(joinedload(
            'user')).all()
    response = []
    for cart in query:
          response.append({**cart.json(), "user": cart.user.json()})
    return response
