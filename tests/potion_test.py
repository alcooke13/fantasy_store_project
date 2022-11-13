import unittest

from models.potion import Potion

class TestPotion(unittest.TestCase):
    def setUp(self):
        self.potion_1 = Potion("Potion of healing", "testing description", 10, 20, 35)

    def test_potion_has_name(self):
        self.assertEqual("Potion of healing", self.potion_1.name)

    def test_potion_has_description(self):
        self.assertEqual("testing description", self.potion_1.description)

    def test_potion_has_quantity(self):
        self.assertEqual(10, self.potion_1.quantity)

    def test_potion_has_cost(self):
        self.assertEqual(20, self.potion_1.cost)

    def test_potion_has_price(self):
        self.assertEqual(35, self.potion_1.price)

    def test_potion_has_id(self):
        self.assertEqual(None, self.potion_1.id)