from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate
from models.db import db
from resources import user, item
app = Flask(__name__)
api = Api(app)


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://localhost:5432/zerowaste"
app.config['SQLALCHEMY_ECHO'] = True


db.init_app(app)
migrate = Migrate(app, db)

api.add_resource(user.Users, "/api/users")
api.add_resource(user.UserInfo, "/api/users/<int:user_id>")

api.add_resource(item.Items, "/api/items")
api.add_resource(item.ItemInfo, "/api/items/<int:item_id>")

if __name__ == '__main__':
    app.run(debug=True)