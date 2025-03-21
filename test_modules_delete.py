import unittest
from models import db, Product
from tests.factories import ProductFactory

class TestProductModel(unittest.TestCase):
    def setUp(self):
        self.product = ProductFactory()
        db.session.add(self.product)
        db.session.commit()

    def test_delete_product(self):
        product = Product.query.get(self.product.id)
        db.session.delete(product)
        db.session.commit()

        deleted_product = Product.query.get(self.product.id)
        self.assertIsNone(deleted_product)

    def tearDown(self):
        db.session.rollback()
