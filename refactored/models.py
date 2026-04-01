"""
This module defines the data models for the E-commerce Shopping Cart system.
It includes Product and CartItem classes to represent store inventory and user selections.
"""

class Product:
    """Represents a physical product available in the store inventory."""
    def __init__(self, product_id, name, price, stock):
        """
        Initializes a Product instance.
        :param product_id: Unique identifier for the product
        :param name: Display name of the product
        :param price: Unit price of the product
        :param stock: Current quantity available in the warehouse
        """
        self.product_id = product_id  # Changed 'id' to 'product_id' to fix Pylint warning
        self.name = name
        self.price = price
        self.stock = stock

class CartItem:
    """Represents a specific product added to a user's shopping cart."""
    def __init__(self, product, quantity, price):
        """
        Initializes a CartItem instance.
        :param product: The Product object
        :param quantity: Number of units selected
        :param price: The price at the time of addition (accounting for discounts)
        """
        self.product = product
        self.quantity = quantity
        self.price = price
        self.total = price * quantity