from flask import Flask, Blueprint
from flask_restplus import Api, Resource
from flask_jwt_extended import JWTManager
from instance.config import app_config
from app.api.v1.views.products import Products, GetSingleProduct
# from app.api.v1.views.sales import Sales, GetSingleSale
# from app.api.v1.views.users import auth
# app = Flask(__name__, instance_relative_config=True)
# obtain the blueprint by initialising
# sales = Blueprint('sales', __name__, url_prefix='/api/v1')
# v1 = Blueprint('sales', __name__, url_prefix='/api/v1')
# products = Blueprint('products', __name__, url_prefix='/api/v1/products')

# api = Api(sales)
# api = Api(app)

def create_app(config_name):
    # app = Flask(__name__, instance_relative_config=True)
    # app.config.from_object(app_config['development'])
    
    # register the blueprint
    # app.register_blueprint(v1)
    # app.register_blueprint(sales)

    # specific endpoints
    # api.add_resource(Sales, '/sales')
    # api.add_resource(GetSingleSale, '/sales/<salesId>')
    # api.add_resource(Products, '/products')
    # api.add_resource(GetSingleProduct, '/products/<productId>')

    app = Flask(__name__)
    api = Api(app)
    
    return app