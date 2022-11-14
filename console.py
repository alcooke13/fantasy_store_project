import pdb

from models.armor import Armor
from models.potion import Potion
from models.weapon import Weapon

import repositories.product_repository as product_repository

# product_repository.delete_all()

# bronze_sword = Weapon("Bronze Sword", "Low tier Sharp Weapon", 20, 75, 100)
# silver_axe = Weapon("Silver Axe", "Low tier Sharp Weapon", 15, 75, 100)
# healing_potion = Potion("Potion of Healing", "Heals all wounds", 40, 25, 45)
# mana_potion = Potion("Mana Potion", "Restores a large amount of Mana", 25, 25, 45)
# light_armor = Armor("Light Armor Set", "Set of armor with low defensive stats", 12, 150, 180)
# heavy_armor = Armor("Heavy Armor Set", "High defensive capabilities with low mobility", 15, 250, 290)

# product_repository.save(bronze_sword)
# product_repository.save(silver_axe)
# product_repository.save(healing_potion)
# product_repository.save(mana_potion)
# product_repository.save(light_armor)
# product_repository.save(heavy_armor)

# pdb.set_trace