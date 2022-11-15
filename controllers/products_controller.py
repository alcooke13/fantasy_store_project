from flask import Blueprint, render_template, redirect, request
import repositories.product_repository as product_repository
import repositories.product_type_repository as product_type_repository
from models.product import Product
products_blueprint = Blueprint("products", __name__)

# Lists all products
@products_blueprint.route("/products")
def products():
    products = product_repository.select_all()
    return render_template("products/index.html", products=products)

# Page to add new product
@products_blueprint.route("/products/new")
def new_product():
    product_types = product_type_repository.select_all()
    return render_template("products/new.html", product_types=product_types)

# Create new page and redirect to products page
@products_blueprint.route("/products", methods=["POST"])
def create_product():
    name = request.form['name']
    description = request.form['description']
    cost = request.form['cost']
    price = request.form['price']
    product_type_id = request.form['type_id']
    product_type = product_type_repository.select(product_type_id)
    new_product = Product(name, description, cost, price, product_type)
    product_repository.save(new_product)
    return redirect("/products")

# Deletes a product
@products_blueprint.route("/products/<id>/delete", methods=['POST'])
def delete_product(id):
    product_repository.delete(id)
    return redirect("/products")

# Show a product
@products_blueprint.route("/products/<id>")
def show_product(id):
    product = product_repository.select(id)
    return render_template("products/show.html", product = product)