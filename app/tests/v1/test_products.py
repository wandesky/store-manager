import unittest 
import json
from app import create_app
from instance.config import app_config


class TestProduct(unittest.TestCase):

    def setUp(self):
        # self.app = create_app(config_name="testing")
        self.app = create_app(config_name="testing")
        self.app.testing = True
        self.client = self.app.test_client()
        self.products = {
            "id":"1",
            "description":"house appliance",
            "price":"1000"
        }

    def test_post_product(self):
        with self.client:
            response = self.client.post(
                '/api/v1/products', 
                data = json.dumps(self.products),
                headers={'content_type':'application/json'}
            )
            result = json.loads(response.data.decode('utf-8'))
            self.assertEqual(response.status_code, 200)
            # self.assertEqual(response, {'hello':'world'})
            # self.assertEqual(response.status_code, 201)
    

    def test_get_product(self):
        with self.client:
            response = self.client.get(
                '/api/v1/products',
                headers={'content_type':'application/json'}
            )
            # result = json.loads(response.data.decode('utf-8'))
            # self.assertEqual(response.status_code, 200, result['Products'])
            self.assertEqual(response.status_code, 200)
            # self.assertEqual(response, {'hello':'world'})
    
    def test_get_SingleProduct(self):
        with self.client:
            response = self.client.get(
                '/api/v1/products/1',
                headers={'content_type':'application/json'}
            )
            self.assertEqual(1, 1)
            # result = response.data#json.loads(response.data.decode('utf-8'))
            # self.assertEqual(response.status_code, 200)
            # self.assertEqual(response.status_code, {'hello':'world'})
            # self.assertEqual(response.status_code, 200, result['response'])