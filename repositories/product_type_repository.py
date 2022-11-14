from db.run_sql import run_sql
from models.product_type import Product_type

def save(product_type):
    sql = "INSERT INTO product_types (name) VALUES (%s) RETURNING *"
    values = [product_type.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    product_type.id = id
    return product_type

def select_all():
    product_types = []
    sql = "SELECT * FROM product_types"
    results = run_sql(sql)
    for result in results:
        product_type = Product_type(result["name"], result["id"])
        product_types.append(product_type)
    return product_types

def select(id):
    sql = "SELECT * FROM product_types WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
    product_type = Product_type(result["name"], result["id"])
    return product_type

def delete_all():
    sql = "DELETE FROM product_types"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM product_types WHERE id = %s"
    values = [id]
    run_sql(sql, values)