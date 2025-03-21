import unittest
from models import db, Product
from tests.factories import ProductFactory

class TestProductModel(unittest.TestCase):
    def setUp(self):
        self.product = ProductFactory()
        db.session.add(self.product)
        db.session.commit()

    def test_read_product(self):
        product = Product.query.get(self.product.id)
        self.assertIsNotNone(product)
        self.assertEqual(product.name, self.product.name)
        self.assertEqual(product.price, self.product.price)

    def tearDown(self):
        db.session.rollback()
