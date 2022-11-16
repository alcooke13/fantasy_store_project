from flask import Blueprint, render_template
import repositories.product_repository as product_repository
import repositories.potion_repository as potion_repository
potions_blueprint = Blueprint("potions", __name__)

# Filter to Potions
@potions_blueprint.route("/products/potions")
def show_potions():
    products = product_repository.select_all()
    potions = potion_repository.select_potions(products)
    counter = potion_repository.count_potions(potions)
    # counter returns a list of numbers in the order of health, mana, strength
    return render_template("/products/potions.html", potions = potions, counter = counter)