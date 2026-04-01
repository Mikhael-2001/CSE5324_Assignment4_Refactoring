"""
This module contains the main ShoppingCart logic.
It manages the collection of items and calculates totals.
"""
from refactored.models import CartItem

class ShoppingCart:
    """Manages a collection of products selected by a user."""
    def __init__(self):
        """Initializes an empty shopping cart."""
        self.items = []

    def add_item(self, product, quantity, price):
        """
        Adds a product to the cart using the CartItem model.
        :param product: The Product object to add
        :param quantity: Quantity to purchase
        :param price: Final price after discounts
        """
        item = CartItem(product, quantity, price)
        self.items.append(item)

    def calculate_subtotal(self):
        """
        Calculates the sum of all items currently in the cart.
        :return: Total cost of items
        """
        return sum(item.total for item in self.items)

    def clear(self):
        """Removes all items from the shopping cart."""
        self.items = []