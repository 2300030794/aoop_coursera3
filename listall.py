import unittest
from models import db, Product
from app import app
from tests.factories import ProductFactory

class TestProductRoutes(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.product = ProductFactory()
        db.session.add(self.product)
        db.session.commit()

    def test_list_all_products(self):
        response = self.app.get("/products")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.json) > 0)

    def tearDown(self):
        db.session.rollback()
