from flask import Flask, request
from flask_restful import Api
from flask_jwt_extended import JWTManager

from resources.user import UserRegister, User, UserLogin
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'jose'
api = Api(app)

@app.before_first_request
def create_tables():
	db.create_all()

jwt = JWTManager(app)  

@jwt.user_claims_loader
def add_claims_to_jwt(identity):
	if identity == 1: ## should read a documentation
		return {'is_admin':True}
	return {'is_admin':False}

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')
api.add_resource(User, '/user/<int:user_id>')
api.add_resource(UserLogin, '/login')

if __name__ == '__main__':
	from db import db
	db.init_app(app)
	app.run(debug=True)  # important to mention debug=True
