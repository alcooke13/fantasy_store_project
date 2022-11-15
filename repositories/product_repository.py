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


# UPDATE products SET name = 'Health Potion', description = 'Updated Potion', cost = '500', price = '550', type_id = '44'
# WHERE id = 64;
