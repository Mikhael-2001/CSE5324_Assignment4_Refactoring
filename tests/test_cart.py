import unittest
from refactored.shopping_cart import ShoppingCart
from refactored.models import Product, CartItem
from refactored.services import VisaPayment, EmailService

class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        """Set up a fresh cart and product for each test."""
        self.cart = ShoppingCart()
        self.test_product = Product(id=1, name="Laptop", price=1000.0, stock=10)

    def test_add_item_to_cart(self):
        """Test if items are correctly added to the cart list."""
        self.cart.add_item(self.test_product, quantity=2, price=900.0)
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.items[0].quantity, 2)
        self.assertEqual(self.cart.items[0].total, 1800.0)

    def test_calculate_subtotal(self):
        """Test the subtotal calculation for multiple items."""
        self.cart.add_item(self.test_product, 1, 1000.0)
        self.cart.add_item(self.test_product, 2, 500.0)
        # 1000 + (2 * 500) = 2000
        self.assertEqual(self.cart.calculate_subtotal(), 2000.0)

    def test_clear_cart(self):
        """Test if the cart is successfully emptied."""
        self.cart.add_item(self.test_product, 1, 1000.0)
        self.cart.clear()
        self.assertEqual(len(self.cart.items), 0)

    def test_visa_payment_strategy(self):
        """Test the Strategy Pattern implementation for Visa."""
        payment = VisaPayment()
        result = payment.process_payment(amount=100.0, card_number="1234-5678")
        self.assertTrue(result)

    def test_email_notification_service(self):
        """Test if the notification service executes without errors."""
        service = EmailService()
        # This confirms the method exists and handles inputs
        try:
            service.send("student@uta.edu", "Order Update", "Your item was added.")
            executed = True
        except Exception:
            executed = False
        self.assertTrue(executed)

if __name__ == '__main__':
    unittest.main()