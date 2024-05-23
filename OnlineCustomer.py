from OrderManagement import OrderManagement
from Menu import Menu
from Order import Order
from BankCard import BankCard
from Receipt import Receipt
from Reservation import Reservation

class OnlineCustomer(OrderManagement):
    def __init__(self, menu, customer_name, delivery_id, kitchen, online_system):
        super().__init__(menu, online_system)
        self.customer_name = customer_name
        self.delivery_id = delivery_id
        self.order = self.create_order("delivery", customer_name, kitchen)
        self.reservation = None
        self.payment_status = False
        self.kitchen = kitchen

    def make_reservation(self, date, time, guests): #Allows the customer to make a reservation online
        self.reservation = Reservation(self.customer_name, date, time, guests)
        available = self.reservation.make_reservation(date, time, guests)
        if available:
            print("Reservation made successfully.")
        else:
            print("Failed to make reservation.")
            self.reservation = None

    def track_order_status(self):
        if self.order:
            self.order.display_order_statuses()
        else:
            print("No active order to track.")

    def place_order(self):
        if self.payment_status:
            if self.order:
                self.order.send_to_kitchen(self.kitchen)
                print(f"Order placed successfully with ID {self.order.order_id}")
            else:
                print("Failed to place order.")
        else:
            print("Payment must be confirmed before placing the order.")

    def make_payment(self):
        correct_amount = self.order.total_cost
        print(f"The exact payment amount required is: ${correct_amount:.2f}")

        while not self.payment_status:
            try:
                amount = float(input("Enter the exact amount to pay: "))
                if amount == correct_amount:
                    payment = BankCard(self.order)
                    if payment.make_payment(amount):
                        self.payment_status = True
                        print("Payment successful.")
                        self.place_order()  # Automatically place the order if payment is successful

                        break
                    else:
                        print("Payment processing failed. Please try again.")
                else:
                    print(f"Please enter the exact amount of ${correct_amount:.2f}.")
            except ValueError:
                print("Invalid input. Please enter a valid amount.")

    def view_receipt(self):
        # Generate and print the receipt
        receipt = Receipt(self.order, "Bank Card")
        receipt.generate_receipt()
