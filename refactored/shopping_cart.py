from refactored.models import CartItem
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity, price):
        item = CartItem(product, quantity, price)
        self.items.append(item)

    def calculate_subtotal(self):
        return sum(item.total for item in self.items)

    def clear(self):
        self.items = []