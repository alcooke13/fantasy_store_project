import unittest

from models.armor import Armor

class TestArmor(unittest.TestCase):
    def setUp(self):
        self.armor_1 = Armor("Light Armor Set", "Provides slight physical resistance and slight magic resistance, no mobility penalty", 5, 125, 175)
        self.armor_2 = Armor("Medium Armor Set", "Provides strong physical resistance and medium magic resistance, lowers mobility slightly", 10, 180, 225)

    def test_armor_has_name(self):
        self.assertEqual("Light Armor Set", self.armor_1.name)

    def test_armor_has_description(self):
        self.assertEqual("Provides slight physical resistance and slight magic resistance, no mobility penalty", self.armor_1.description)

    def test_armor_has_quantity(self):
        self.assertEqual(10, self.armor_2.quantity)

    def test_armor_has_cost(self):
        self.assertEqual(125, self.armor_1.cost)

    def test_armor_has_price(self):
        self.assertEqual(175, self.armor_1.price)