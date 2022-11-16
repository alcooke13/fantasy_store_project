from flask import Blueprint, render_template, redirect, request, url_for
import repositories.product_repository as product_repository
import repositories.product_type_repository as product_type_repository
from models.product import Product
potions_blueprint = Blueprint("potions", __name__)
import pdb

# Filter to Potions
@potions_blueprint.route("/products/potions")
def show_potions():
    products = product_repository.select_all()
    potions = product_repository.select_potions(products)
    counter = product_repository.count_potions(potions)
    # counter returns a list of numbers in the order of health, mana, strength
    return render_template("/products/potions.html", potions = potions, counter = counter)