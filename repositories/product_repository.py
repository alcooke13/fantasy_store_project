from db.run_sql import run_sql
from models.product import Product
from models.product_type import Product_type
import repositories.product_type_repository as product_type_repository

def save(product):
    sql = "INSERT INTO products (name, description, cost, price, type_id) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [product.name, product.description, product.cost, product.price, product.product_type.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    product.id = id
    return product

def select(id):
    sql = "SELECT * FROM products WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        product_type = product_type_repository.select(result["product_type_id"])
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
    
