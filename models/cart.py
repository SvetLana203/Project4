from datetime import datetime
from models.db import db

class Cart(db.Model):
  __tablename__ = "carts"

  id = db.Column(db.Integer, primary_key=True)
  created_at = db.Column(db.DateTime, default=str(
        datetime.utcnow()), nullable=False)
  updated_at = db.Column(db.DateTime, default=datetime.utcnow(
    ), nullable=False, onupdate=datetime.now())
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

  def __init__(self, user_id):
    self.user_id = user_id

  def json(self):
    return {
      "id": self.id,
      "created_at": str(self.created_at),
      "updated_at": str(self.updated_at)
    }