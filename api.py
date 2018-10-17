from flask import Flask
from flask_restplus import Api, Resource, fields
from werkzeug.contrib.fixers import ProxyFix

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
api = Api(app, version='1', title='Store Manager API',
    description='Backend code for the Andela Store Manager Challenge',
    )

products_ns = api.namespace('products', description='Product operations')

product = api.model('Product', {
    'id':fields.Integer(readOnly = True, description='The product unique identifier'),
    'details':fields.String(required=True, description='Product details')
})

class ProductDataAccessObject(object):
    def __init__(self):
        self.counter = 0
        self.products = []

    def get(self, id):
        for product in self.products:
            if product['id'] == id:
                return product
            api.abort(404, "Product {} does not exist".format(id))

    def create(self, data):
        product = data
        product['id'] = self.counter = self.counter + 1
        self.products.append(product)
        return product

    def update(self, id, data):
        product = self.get(id)
        product.update(data)
        return product

    def delete(self, id):
        product = self.get(id)
        self.products.remove(product)

DemoProduct = ProductDataAccessObject()
DemoProduct.create({'product':'Spoon'})
DemoProduct.create({'product':'Cup'})
DemoProduct.create({'product':'Jug'})

@products_ns.route('/')
class ProductList(Resource):
    '''Displays a list of all products with provision to POST a new product'''
    @products_ns.doc('list_products')
    def get(self):
        '''List all products'''
        return DemoProduct.products
    
    @products_ns.doc('create_product')
    @products_ns.expect(product)
    @products_ns.marshal_with(product, code=201)
    def post(self):
        '''Create a new product'''
        return DemoProduct.create(api.payload), 201

    @products_ns.route('/<int:id>')
    @products_ns.response(404, 'Product not found')
    @products_ns.param('id', 'Unique identifier of the product')
    class Product(Resource):
        '''Show a single product with provision for deleting products'''
        @products_ns.doc('get_product')
        @products_ns.marshal_with(product)
        def get(self, id):
            '''Fetch a given resource'''
            return DemoProduct.get(id)

        @products_ns.doc('delete_product')
        @products_ns.response(204, 'Product deleted')
        def delete(self, id):
            '''Delete a product using its identifier'''
            DemoProduct.delete(id)
            return '', 204

        @products_ns.expect(product)
        @products_ns.marshal_with(product)
        def put(self, id):
            '''Update a product using its identifier'''
            return DemoProduct.update(id, api.payload)

    if __name__ == '__main__':
        app.run(debug=True)