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

    def test_read_product(self):
        response = self.app.get(f"/products/{self.product.id}")
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.product.name, response.get_data(as_text=True))

    def tearDown(self):
        db.session.rollback()
