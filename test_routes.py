import unittest
import json
from models import db, Product
from app import app
from tests.factories import ProductFactory

class TestProductRoutes(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.product = ProductFactory()
        db.session.add(self.product)
        db.session.commit()

    def test_update_product(self):
        updated_data = {"name": "Updated Name"}
        response = self.app.put(
            f"/products/{self.product.id}",
            data=json.dumps(updated_data),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("Updated Name", response.get_data(as_text=True))

    def tearDown(self):
        db.session.rollback()
