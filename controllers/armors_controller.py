from flask import Blueprint, render_template, redirect, request, url_for
import repositories.product_repository as product_repository
import repositories.product_type_repository as product_type_repository
from models.product import Product
armors_blueprint = Blueprint("armors", __name__)
import pdb

# Filter to Armors
@armors_blueprint.route("/products/armors")
def show_armors():
    products = product_repository.select_all()
    armors = product_repository.select_armor(products)
    counter = product_repository.count_armor(armors)
    # counter returns a list of numbers in the order of light, medium, heavy
    return render_template("/products/armors.html", armors = armors, counter = counter)