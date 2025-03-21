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

    def test_delete_product(self):
        response = self.app.delete(f"/products/{self.product.id}")
        self.assertEqual(response.status_code, 204)

        deleted_product = Product.query.get(self.product.id)
        self.assertIsNone(deleted_product)

    def tearDown(self):
        db.session.rollback()
