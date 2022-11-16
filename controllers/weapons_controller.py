from flask import Blueprint, render_template
import repositories.product_repository as product_repository
import repositories.weapon_repository as weapon_repository
weapons_blueprint = Blueprint("weapons", __name__)
import pdb

@weapons_blueprint.route("/products/weapons")
def show_weapons():
    products = product_repository.select_all()
    weapons = weapon_repository.select_weapons(products)
    counter = weapon_repository.count_weapons(weapons)
    #counter returns a list of numbers in the order of sword, axe, spear, shield
    return render_template("products/weapons.html", weapons = weapons, counter = counter)