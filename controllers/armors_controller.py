from flask import Blueprint, render_template
import repositories.product_repository as product_repository
import repositories.armor_repository as armor_repository
armors_blueprint = Blueprint("armors", __name__)

# Filter to Armors
@armors_blueprint.route("/products/armors")
def show_armors():
    products = product_repository.select_all()
    armors = armor_repository.select_armor(products)
    counter = armor_repository.count_armor(armors)
    # counter returns a list of numbers in the order of light, medium, heavy
    return render_template("/products/armors.html", armors = armors, counter = counter)