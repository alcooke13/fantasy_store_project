class Armor:
    def __init__(self, name, description, quantity, cost, price, id = None):
        self.name = name
        self.description = description
        self.quantity = quantity
        self.cost = cost
        self.price = price
        self.id = id

    def armor_quantity_decreases(self):
        self.quantity -= 1

    def armor_quantity_increases(self):
        self.quantity += 1