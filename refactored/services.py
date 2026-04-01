"""
This module contains the business logic services for the shopping cart.
It implements the Strategy Pattern for payments and an Email Notification service.
"""
from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    """Abstract base class for all payment processing methods."""
    @abstractmethod
    def process_payment(self, amount, card_number):
        """Method to be implemented by concrete payment strategies."""
        pass

class VisaPayment(PaymentStrategy):
    """Concrete implementation of payment processing using Visa cards."""
    def process_payment(self, amount, card_number):
        """Simulates processing a Visa transaction."""
        print(f"Processing ${amount} via Visa for card {card_number}")
        return True

class EmailService:
    """Handles sending automated email notifications to customers."""
    def send(self, email, subject, body):
        """
        Sends a simulated email.
        :param email: Recipient address
        :param subject: Email subject line
        :param body: Email message content
        """
        print(f"Sending email to {email}: {subject}\nContent: {body}")