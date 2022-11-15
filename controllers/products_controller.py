from flask import Blueprint, render_template, redirect, request, url_for
import repositories.product_repository as product_repository
import repositories.product_type_repository as product_type_repository
from models.product import Product
products_blueprint = Blueprint("products", __name__)
import pdb

# Lists all products
@products_blueprint.route("/products")
def products():
    weapon_counter = 0
    potion_counter = 0
    armor_counter = 0
    products = product_repository.select_all()
    pdb.set_trace()
    for product in products:
        if product.product_type.name == "Weapons":
            weapon_counter += 1
        if product.product_type.name == "Potions":
            potion_counter += 1
        if product.product_type.name == "Armor":
            armor_counter += 1
    return render_template("products/index.html", products=products, weapon_counter = weapon_counter, potion_counter=potion_counter, armor_counter=armor_counter)

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

# Edit a product
@products_blueprint.route("/products/<id>/edit")
def edit_product(id):
    product = product_repository.select(id)
    product_types = product_type_repository.select_all()
    return render_template("products/edit.html", product = product, product_types = product_types)

# Update a product

@products_blueprint.route("/products/<id>", methods=["POST"])
def update_product(id):
    name = request.form['product_name']
    description = request.form['description']
    cost = request.form['cost']
    price = request.form['price']
    product_type_id = request.form['type_id']
    product_type = product_type_repository.select(product_type_id)
    updated_product = Product(name, description, cost, price, product_type, id)
    product_repository.update(updated_product)
    # return redirect(url_for("products.show_product", id=id))
    return redirect(f"/products/{id}")
