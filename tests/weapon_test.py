import unittest

from models.weapon import Weapon

class TestWeapon(unittest.TestCase):
    def setUp(self):
        self.weapon_1 = Weapon("Bronze Sword", "testing sword description", 3, 100, 150)

    def test_weapon_has_name(self):
        self.assertEqual("Bronze Sword", self.weapon_1.name)

    def test_weapon_has_description(self):
        self.assertEqual("testing sword description", self.weapon_1.description)

    def test_weapon_has_quantity(self):
        self.assertEqual(3, self.weapon_1.quantity)

    def test_weapon_has_cost(self):
        self.assertEqual(100, self.weapon_1.cost)

    def test_weapon_has_price(self):
        self.assertEqual(150, self.weapon_1.price)

    def test_weapon_has_id(self):
        self.assertEqual(None, self.weapon_1.id)