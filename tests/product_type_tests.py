import unittest
from models.product_type import Product_type

class TestProduct_type(unittest.TestCase):
    def setUp(self):
        self.weapon = Product_type("Weapon")

    def test_product_type_has_name(self):
        self.assertEqual("Weapon", self.weapon.name)

    def test_product_type_has_id(self):
        self.assertEqual(None, self.weapon.id)
