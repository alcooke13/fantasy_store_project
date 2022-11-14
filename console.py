import pdb

from models.product import Product
import repositories.product_repository as product_repository

product_repository.delete_all()

bronze_sword = Product("Bronze Sword", "Low tier Sharp Weapon", 75, 100, "Weapon")
silver_axe = Product("Silver Axe", "Low tier Sharp Weapon", 75, 100, "Weapon")
healing_potion = Product("Potion of Healing", "Heals all wounds", 25, 45, "Potion")
mana_potion = Product("Mana Potion", "Restores a large amount of Mana", 25, 45, "Potion")
light_armor = Product("Light Armor Set", "Set of armor with low defensive stats", 150, 180, "Armor")
heavy_armor = Product("Heavy Armor Set", "High defensive capabilities with low mobility", 250, 290, "Armor")

product_repository.save(bronze_sword)
product_repository.save(silver_axe)
product_repository.save(healing_potion)
product_repository.save(mana_potion)
product_repository.save(light_armor)
product_repository.save(heavy_armor)

# pdb.set_trace