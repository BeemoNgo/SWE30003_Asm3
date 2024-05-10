from OrderManagement import OrderManagement
from Order import Order
from Reservation import Reservation

class OnlineCustomer(OrderManagement):
    def __init__(self, customer_name, delivery_id):
        super().__init__(customer_name)
        self.delivery_id = delivery_id

    def create_order(self, order_id):
        new_order = Order(order_id, delivery_id=self.delivery_id)
        self.add_order(new_order)

    # def make_reservation():

    # def track_order(self, order):
    #     print(f"Order ID: {order.order_id} - Status: {order.status()}")
    #     for item in order.items:
    #         print(f"{item.status} - {item.menu.get_item(item.item_id)['description']}")

    # def make_payment(self, order):
    #     order.mark_as_paid()
    #     print(f"Payment processed for Order ID: {order.order_id}")