import unittest
from service import app
from service.models import db, Product

class TestProductRoutes(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
        self.app = app.test_client()
        with app.app_context():
            db.create_all()
            self.product = Product(name="Test Product", category="Test Category", available=True)
            db.session.add(self.product)
            db.session.commit()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_list_by_category(self):
        response = self.app.get(f"/products?category={self.product.category}")
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.product.category, response.get_data(as_text=True))

if __name__ == "__main__":
    unittest.main()
