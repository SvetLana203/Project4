from datetime import datetime
from models.db import db
from sqlalchemy.orm import joinedload

class Item(db.Model):
  __tablename__ = "items"

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255), nullable=False)
  image = db.Column(db.String(255), nullable=False)
  description = db.Column(db.String(255), nullable=False)
  created_at = db.Column(db.DateTime, default=str(
        datetime.utcnow()), nullable=False)
  updated_at = db.Column(db.DateTime, default=datetime.utcnow(
    ), nullable=False, onupdate=datetime.now())
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  user = db.relationship("User", backref=db.backref('users', lazy=True))

  def __init__(self, name, image, description, user_id):
    self.name = name
    self.image = image
    self.description = description
    self.user_id = user_id

  def json(self):
    return {
      "id": self.id,
      "name": self.name,
      "image": self.image,
      "description": self.description,
      "created_at": str(self.created_at),
      "updated_at": str(self.updated_at)
    }

  def create(self):
    db.session.add(self)
    db.session.commit()
    return self

  @classmethod
  def find_all(cls):
    query = Item.query.options(joinedload("user")).all()
    response = []
    for item in query:
      response.append({**item.json(), "user": item.user.json()})
    return response

  @classmethod
  def find_by_id(cls, item_id):
    item = Item.query.filter_by(id=item_id).first()
    return item