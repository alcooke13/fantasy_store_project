import pdb

from models.product import Product
import repositories.product_repository as product_repository
from models.product_type import Product_type
import repositories.product_type_repository as product_type_repository

product_repository.delete_all()
product_type_repository.delete_all()

type_weapon = Product_type("Weapons")
type_potion = Product_type("Potions")
type_armor = Product_type("Armor")

product_type_repository.save(type_weapon)
product_type_repository.save(type_potion)
product_type_repository.save(type_armor)

# test = product_type_repository.select(23)

bronze_sword = Product("Bronze Sword", "Low tier Sharp Weapon", 75, 100, type_weapon)
silver_axe = Product("Silver Axe", "Low tier Sharp Weapon", 75, 100, type_weapon)
healing_potion = Product("Potion of Healing", "Heals all wounds", 25, 45, type_potion)
mana_potion = Product("Mana Potion", "Restores a large amount of Mana", 25, 45, type_potion)
light_armor = Product("Light Armor Set", "Set of armor with low defensive stats", 150, 180, type_armor)
heavy_armor = Product("Heavy Armor Set", "High defensive capabilities with low mobility", 250, 290, type_armor)

product_repository.save(bronze_sword)
product_repository.save(silver_axe)
product_repository.save(healing_potion)
product_repository.save(mana_potion)
product_repository.save(light_armor)
product_repository.save(heavy_armor)

# results = product_type_repository.select_all()
# for result in results:
#     print(result.name)

# results = product_repository.select_all()
# for result in results:
#     print(result)

# pdb.set_trace()