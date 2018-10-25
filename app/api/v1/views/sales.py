from flask import Flask
from flask_restplus import Api, Resource, fields
from werkzeug.contrib.fixers import ProxyFix

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
api = Api(app, version='1', title='Store Manager API',
    description='Backend code for the Andela Store Manager Challenge',
    )

sales_ns = api.namespace('sales', description='Sale operations')

sale = api.model('Sale', {
    'id':fields.Integer(readOnly = True, description='The sale unique identifier'),
    'product-id':fields.Integer(required=True, description='The id of the item sold'),
    'attendant':fields.String(required=True, description='The attendant who made the sale')
})

class SaleDataAccessObject(object):
    def __init__(self):
        self.counter = 0
        self.sales = []

    def get(self, id):
        for sale in self.sales:
            if sale['id'] == id:
                return sale
            api.abort(404, "Sale record {} does not exist".format(id))

    def create(self, data):
        sale = data
        # sale['id'] = self.counter + 1
        self.counter = self.counter + 1
        self.sales.append(sale)
        return sale

    def update(self, id, data):
        sale = self.get(id)
        sale.update(data)
        return sale

    def delete(self, id):
        sale = self.get(id)
        self.sales.remove(sale)

DemoSale = SaleDataAccessObject()
DemoSale.create({'sale':'Spoon'})
DemoSale.create({'sale':'Cup'})
DemoSale.create({'sale':'Jug'})

@sales_ns.route('/')
class Sales(Resource):
    '''Displays a list of all sales with provision to POST a new sale'''
    @sales_ns.doc('list_sales')
    def get(self):
        '''List all sales records'''
        return DemoSale.sales
    
    @sales_ns.doc('create a_sale')
    @sales_ns.expect(sale)
    @sales_ns.marshal_with(sale, code=201)
    def post(self):
        '''Create a new sale record'''
        return DemoSale.create(api.payload), 201

@sales_ns.route('/<int:id>')
@sales_ns.response(404, 'Sale record not found not found')
@sales_ns.param('id', 'Unique identifier of the sold item')
class Sale(Resource):
    '''Show a single sale with provision for deleting existing sales'''
    
    @sales_ns.doc('get_sale')
    @sales_ns.marshal_with(sale)
    def get(self, id):
        '''Fetch a given resource'''
        return DemoSale.get(id)

    @sales_ns.doc('create_sale')
    @sales_ns.marshal_with(sale)
    def post(self, id):
        '''Fetch a given resource'''
        return DemoSale.create(id)

    @sales_ns.doc('delete_sale')
    @sales_ns.response(204, 'Sale deleted')
    def delete(self, id):
        '''Delete a sale using its identifier'''
        DemoSale.delete(id)
        return '', 204

    @sales_ns.expect(sale)
    @sales_ns.marshal_with(sale)
    def put(self, id):
        '''Update a sale using its identifier'''
        return DemoSale.update(id, api.payload)

if __name__ == '__main__':
    app.run(debug=True)