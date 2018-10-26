from flask import Flask, Blueprint
from flask_restplus import Api, Resource, fields
from flask_jwt_extended import JWTManager
from instance.config import app_config
from werkzeug.contrib.fixers import ProxyFix
from app.api.v1.views.products import Products, Product 
from app.api.v1.views.sales import Sales, Sale

def create_app(config_name):
    app = Flask(__name__)
    app.wsgi_app = ProxyFix(app.wsgi_app)
    api = Api(app, version='1', title='Store Manager API',
        description='Backend code for the Andela Store Manager Challenge',
        )

    products_ns = api.namespace('products', description='Product operations')

    product = api.model('Product', {
        'id':fields.String(readOnly = True, description='The product unique identifier'),
        'details':fields.String(required=True, description='Product details')
    })

    sales_ns = api.namespace('sales', description='Sale operations')

    sale = api.model('Sale', {
        'id':fields.String(readOnly = True, description='The sale unique identifier'),
        'product-id':fields.String(required=True, description='The id of the sold item'),
        'attendant':fields.String(required=True, description='The attendant who made the sale')
    })

    api.add_resource(Products, '/api/v1/products')
    api.add_resource(Sales, '/api/v1/sales')
    api.add_resource(Product, '/api/v1/products/<int:id>')
    api.add_resource(Sale, '/api/v1/sales/<int:id>')
    
    return app
