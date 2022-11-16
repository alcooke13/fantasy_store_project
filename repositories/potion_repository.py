def select_potions(products):
    potions_list = []
    for product in products:
        if product.product_type.name == "Potions":
            potions_list.append(product)
    return potions_list

def count_potions(potions):
    health_count = 0
    mana_count = 0
    strength_count = 0
    for potion in potions:
        if "Health" in potion.name:
            health_count += 1
        if "Mana" in potion.name:
            mana_count += 1
        if "Strength" in potion.name:
            strength_count += 1
    return [health_count, mana_count, strength_count]