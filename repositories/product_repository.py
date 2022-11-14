# from db.run_sql import run_sql
# from models.product import Product

# def save(weapon):
#     sql = "INSERT INTO products (name) VALUES (%s) RETURNING *"
#     values = [weapon.name]
#     results = run_sql(sql, values)
#     id = results[0]['id']
#     weapon.id = id
#     return weapon


# def delete_all():
#     sql = "DELETE FROM products"
#     run_sql(sql)

# def delete(id):
#     sql = "DELETE FROM products WHERE id = %s"
#     values = [id]
#     run_sql(sql, values)
    
