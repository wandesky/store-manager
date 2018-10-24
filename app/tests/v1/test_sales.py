import unittest 
import json
from app import create_app
from instance.config import app_config


class TestSale(unittest.TestCase):

    def setUp(self):
        self.app = create_app(config_name="testing")
        self.app.testing = True
        self.client = self.app.test_client()
        self.sales = {
            "sale-id":1,
            "product-id":5,
            "attendant":"mutiso"
        }

    def test_get_all_sales(self):
        with self.client:
            response = self.client.get(
                '/api/v1/sales',
                headers={'content_type':'application/json'}
            )
            # result = json.loads(response.data.decode('utf-8'))
            # self.assertEqual(response.status_code, 200, result['Products'])
            self.assertEqual(response.status_code, 200)
            # self.assertEqual(response, {'hello':'world'})

    def test_post_sale(self):
        with self.client:
            response = self.client.post(
                '/api/v1/sales/', 
                data = json.dumps(self.sales),
                headers={'content_type':'application/json'}
            )
            # result = json.loads(response.data.decode('utf-8'))
            # self.assertEqual(response.status_code, 200, result['response'])
            # self.assertEqual(response, {'hello':'world'})
            self.assertEqual(response.status_code, 201)
    
    def test_get_single_sales(self):
        with self.client:
            response = self.client.get(
                '/api/v1/sales/1',
                headers={'content_type':'application/json'}
            )
            # result = response.data#json.loads(response.data.decode('utf-8'))
            self.assertEqual(response.status_code, 200)
            # self.assertEqual(response.status_code, {'hello':'world'})
            # self.assertEqual(response.status_code, 200, result['response'])