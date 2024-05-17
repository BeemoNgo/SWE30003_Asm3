from OrderManagement import OrderManagement
from Menu import Menu
from Order import Order
from Reservation import Reservation

class OnlineCustomer(OrderManagement):
    def __init__(self, menu, customer_name, delivery_id, kitchen, online_system):
        super().__init__(menu, online_system)
        self.customer_name = customer_name
        self.delivery_id = delivery_id
        self.order = self.create_order("delivery", customer_name, kitchen)
        self.reservation = None
        self.payment_status = False

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

    def place_order(self): #Places the order if payment is confirmed
        if self.payment_status:
            self.order = self.create_order("delivery", self.customer_name)
            if self.order:
                print(f"Order placed successfully with ID {self.order.order_id}")
            else:
                print("Failed to place order.")
        else:
            print("Payment must be confirmed before placing the order.")

    def pay_for_order(self):
        self.payment_status = True
        print("Payment confirmed.")