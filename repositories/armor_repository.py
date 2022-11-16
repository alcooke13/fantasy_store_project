def select_armor(products):
    armor_list = []
    for product in products:
        if product.product_type.name == "Armor":
            armor_list.append(product)
    return armor_list

def count_armor(armors):
    light_count = 0
    medium_count = 0
    heavy_count = 0
    for armor in armors:
        if "Light" in armor.name:
            light_count += 1
        if "Medium" in armor.name:
            medium_count += 1
        if "Heavy" in armor.name:
            heavy_count += 1
    return [light_count, medium_count, heavy_count]