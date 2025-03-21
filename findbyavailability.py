import unittest
from models import db, Product
from tests.factories import ProductFactory

class TestProductModel(unittest.TestCase):
    def setUp(self):
        self.product = ProductFactory(available=True)
        db.session.add(self.product)
        db.session.commit()

    def test_find_by_availability(self):
        products = Product.query.filter_by(available=True).all()
        self.assertTrue(len(products) > 0)
        self.assertIn(self.product, products)

    def tearDown(self):
        db.session.rollback()
