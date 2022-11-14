import unittest

from models.product import Product

class TestProduct(unittest.TestCase):
    def setUp(self):
        self.product_1 = Product("Potion of healing", "testing description", 20, 35)

    def test_product_has_name(self):
        self.assertEqual("Potion of healing", self.product_1.name)

    def test_product_has_description(self):
        self.assertEqual("testing description", self.product_1.description)

    def test_product_has_cost(self):
        self.assertEqual(20, self.product_1.cost)

    def test_product_has_price(self):
        self.assertEqual(35, self.product_1.price)

    def test_product_has_id(self):
        self.assertEqual(None, self.product_1.id)