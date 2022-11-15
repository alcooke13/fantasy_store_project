from db.run_sql import run_sql
from models.product import Product
from models.product_type import Product_type
import repositories.product_type_repository as product_type_repository
import repositories.product_repository as product_repository

def save(product):
    sql = "INSERT INTO products (name, description, cost, price, type_id) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [product.name, product.description, product.cost, product.price, product.product_type.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    product.id = id
    return product

def select(id):
    product = None
    sql = "SELECT * FROM products WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        product_type = product_type_repository.select(result["type_id"])
        product = Product(result['name'], result['description'], result['cost'], result['price'], product_type, result["id"])
    return product

def select_all():
    products = []
    sql = "SELECT * FROM products"
    results = run_sql(sql)
    for result in results:
        product_type = product_type_repository.select(result['type_id'])
        product = Product(result['name'], result['description'], result['cost'], result['price'], product_type, result["id"])
        products.append(product)
    return products

def delete_all():
    sql = "DELETE FROM products"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM products WHERE id = %s"
    values = [id]
    run_sql(sql, values)
    
def update(product):
    sql = "UPDATE products SET (name, description, cost, price, type_id) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [product.name, product.description, product.cost, product.price, product.product_type.id, product.id]
    print(values)
    run_sql(sql, values)

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