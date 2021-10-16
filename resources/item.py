from models.db import db
from models.item import Item
from flask_restful import Resource
from flask import request
from sqlalchemy.orm import joinedload

class Items(Resource):
  def get(self):
    items = Item.find_all()
    return items

  def post(self):
    data = request.get_json()
    params = {}
    for k in data.keys():
      params[k] = data[k]
    item = Item(**params)
    item.create()
    return item.json(), 201

class ItemInfo(Resource):
  def get(self, item_id):
      item = Item.query.options(joinedload("user")).filter_by(id=item_id).first()
      return {**item.json(), "user": item.user.json()}

  def put(self, item_id):
      data = request.get_json()
      item = Item.find_by_id(item_id)
      for key in data:
        setattr(item, key, data[key]) 
        db.session.commit() 
      return item.json(), 201

  def delete(self, item_id):
      item = Item. find_by_id(item_id)
      if not item:
        return {"msg": "Not found"}, 404
      db.session.delete(item)
      db.session.commit()
      return {"msg": "Item Deleted", "payload": item_id}

# class ItemImage(Resource):
#   def post(self):
#       file = request.files['file']
#       bucket.Object(file.filename).put(Body=file)
#       return "uploaded"  