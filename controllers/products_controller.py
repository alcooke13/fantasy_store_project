from flask import Blueprint, render_template, redirect
import repositories.product_repository as product_repository
products_blueprint = Blueprint("products", __name__)

# INDEX
@products_blueprint.route("/products")
def products():
    products = product_repository.select_all()
    return render_template("products/index.html", products=products)