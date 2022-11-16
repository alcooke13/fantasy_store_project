def select_weapons(products):
    weapons_list = []
    for product in products:
        if product.product_type.name == "Weapons":
            weapons_list.append(product)
    return weapons_list

def count_weapons(weapons):
    sword_count = 0
    axe_count = 0
    spear_count = 0
    shield_count = 0
    for weapon in weapons:
        if "Sword" in weapon.name:
            sword_count += 1
        if "Axe" in weapon.name:
            axe_count += 1
        if "Spear" in weapon.name:
            spear_count += 1
        if "Shield" in weapon.name:
            shield_count += 1
    return [sword_count, axe_count, spear_count, shield_count]