from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def process_payment(self, amount, card_number):
        pass

class VisaPayment(PaymentStrategy):
    def process_payment(self, amount, card_number):
        print(f"Processing ${amount} via Visa")
        return True

class EmailService:
    def send(self, email, subject, body):
        print(f"Sending email to {email}: {subject}")