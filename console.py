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

bronze_sword = Product("Bronze Sword", "Low tier sharp weapon", 80, 110, type_weapon)
silver_sword = Product("Silver Sword", "Mid tier sharp weapon", 120, 160, type_weapon)
gold_sword = Product("Gold Sword", "High tier sharp weapon", 200, 250, type_weapon)

bronze_axe = Product("Bronze Axe", "Low tier sharp weapon", 80, 110, type_weapon)
silver_axe = Product("Silver Axe", "Mid tier sharp Weapon", 120, 160, type_weapon)
gold_axe = Product("Gold Axe", "High tier sharp Weapon", 200, 250, type_weapon)

bronze_spear = Product("Bronze Spear", "Low tier sharp weapon", 80, 110, type_weapon)
silver_spear = Product("Silver Spear", "Mid tier sharp Weapon", 120, 160, type_weapon)
gold_spear = Product("Gold Spear", "High tier sharp Weapon", 200, 250, type_weapon)

shield = Product("Shield", "Reduces damage taken, adds blocking ability", 150, 185, type_weapon)

healing_potion = Product("Health Potion", "Heals all wounds", 30, 50, type_potion)
mana_potion = Product("Mana Potion", "Restores a large amount of Mana", 25, 45, type_potion)
strength_potion = Product("Strength Potion", "Potion which allows one to go beyond their limits. Increases Attack Power", 30, 50, type_potion)

light_armor = Product("Light Armor", "Low defensive capabilities with great mobility", 150, 190, type_armor)
medium_armor = Product("Medium Armor", "Best of both worlds, moderate defensive capabilities with moderate mobility", 200, 250, type_armor)
heavy_armor = Product("Heavy Armor", "High defensive capabilities with low mobility", 250, 290, type_armor)

for i in range(8):
    product_repository.save(bronze_sword)
for i in range(4):
    product_repository.save(silver_sword)
for i in range(2):
    product_repository.save(gold_sword)

for i in range(5):
    product_repository.save(bronze_axe)
for i in range(6):
    product_repository.save(silver_axe)
for i in range(1):
    product_repository.save(gold_axe)

for i in range(4):
    product_repository.save(bronze_spear)
for i in range(6):
    product_repository.save(silver_spear)
for i in range(6):
    product_repository.save(gold_spear)

for i in range(3):
    product_repository.save(shield)

for i in range(10):
    product_repository.save(healing_potion)
for i in range(8):
    product_repository.save(mana_potion)
for i in range(9):
    product_repository.save(strength_potion)

for i in range(5):
    product_repository.save(light_armor)
for i in range(5):
    product_repository.save(medium_armor)
for i in range(4):
    product_repository.save(heavy_armor)

# results = product_type_repository.select_all()
# for result in results:
#     print(result.name)

# results = product_repository.select_all()
# for result in results:
#     print(result)

# pdb.set_trace()