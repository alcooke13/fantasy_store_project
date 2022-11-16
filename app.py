from flask import Flask, render_template

from controllers.products_controller import products_blueprint
from controllers.potions_controller import potions_blueprint
from controllers.armors_controller import armors_blueprint
from controllers.weapons_controller import weapons_blueprint

app = Flask(__name__)

app.register_blueprint(products_blueprint)
app.register_blueprint(potions_blueprint)
app.register_blueprint(armors_blueprint)
app.register_blueprint(weapons_blueprint)

@app.route("/")
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
