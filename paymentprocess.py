from abc import ABC, abstractmethod
from datetime import datetime

# ----------------------------
# Decorator for logging
# ----------------------------
def log_transaction(func):
    def wrapper(*args, **kwargs):
        print("\n------------------------------")
        print("Transaction Started")
        print("Time :", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
        result = func(*args, **kwargs)
        print("Transaction Completed")
        print("------------------------------\n")
        return result
    return wrapper


# ----------------------------
# Receipt Class
# ----------------------------
class Receipt:

    def __init__(self, method, amount, status):
        self.method = method
        self.amount = amount
        self.status = status

    def __str__(self):
        return f"""
=========== RECEIPT ===========
Payment Method : {self.method}
Amount         : ₹{self.amount}
Status         : {self.status}
===============================
"""


# ----------------------------
# Strategy Abstract Class
# ----------------------------
class PaymentStrategy(ABC):

    @abstractmethod
    def validate(self):
        pass

    @abstractmethod
    def pay(self, amount):
        pass


# ----------------------------
# Credit Card Strategy
# ----------------------------
class CreditCard(PaymentStrategy):

    def __init__(self):
        self.card = input("Enter 16-digit Card Number : ")

    def validate(self):
        return len(self.card) == 16 and self.card.isdigit()

    def pay(self, amount):
        print("Payment via Credit Card Successful.")
        return Receipt("Credit Card", amount, "SUCCESS")


# ----------------------------
# PayPal Strategy
# ----------------------------
class PayPal(PaymentStrategy):

    def __init__(self):
        self.email = input("Enter PayPal Email : ")

    def validate(self):
        return "@" in self.email

    def pay(self, amount):
        print("Payment via PayPal Successful.")
        return Receipt("PayPal", amount, "SUCCESS")


# ----------------------------
# UPI Strategy
# ----------------------------
class UPI(PaymentStrategy):

    def __init__(self):
        self.upi = input("Enter UPI ID : ")

    def validate(self):
        return "@" in self.upi

    def pay(self, amount):
        print("Payment via UPI Successful.")
        return Receipt("UPI", amount, "SUCCESS")


# ----------------------------
# Net Banking Strategy
# ----------------------------
class NetBanking(PaymentStrategy):

    def __init__(self):
        self.bank = input("Enter Bank Name : ")

    def validate(self):
        return len(self.bank) > 2

    def pay(self, amount):
        print("Payment via Net Banking Successful.")
        return Receipt("Net Banking", amount, "SUCCESS")


# ----------------------------
# Context Class
# ----------------------------
class PaymentProcessor:

    registry = {}

    @classmethod
    def register_strategy(cls, name, strategy):
        cls.registry[name] = strategy

    def __init__(self):
        self.strategy = None

    def set_strategy(self, strategy_name):

        strategy_class = self.registry.get(strategy_name)

        if strategy_class:
            self.strategy = strategy_class()
        else:
            print("Invalid Payment Method")

    @log_transaction
    def process_payment(self, amount):

        if self.strategy is None:
            print("No Payment Method Selected.")
            return

        if self.strategy.validate():

            receipt = self.strategy.pay(amount)

        else:

            print("Validation Failed!")

            receipt = Receipt(
                self.strategy.__class__.__name__,
                amount,
                "FAILED"
            )

        print(receipt)


# ----------------------------
# Register Strategies
# ----------------------------
PaymentProcessor.register_strategy("1", CreditCard)
PaymentProcessor.register_strategy("2", PayPal)
PaymentProcessor.register_strategy("3", UPI)
PaymentProcessor.register_strategy("4", NetBanking)


# ----------------------------
# Main Program
# ----------------------------
processor = PaymentProcessor()

while True:

    print("\n========= PAYMENT MENU =========")
    print("1. Credit Card")
    print("2. PayPal")
    print("3. UPI")
    print("4. Net Banking")
    print("5. Exit")

    choice = input("Choose Payment Method : ")

    if choice == "5":
        print("Thank You!")
        break

    if choice not in PaymentProcessor.registry:
        print("Invalid Choice!")
        continue

    processor.set_strategy(choice)

    amount = float(input("Enter Amount : ₹"))

    processor.process_payment(amount)

    again = input("Switch Payment Method? (y/n) : ")

    if again.lower() != "y":
        print("Thank You!")
        break