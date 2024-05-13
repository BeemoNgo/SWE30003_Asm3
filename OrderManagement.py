from Order import Order
from OrderItem import OrderItem

class OrderManagement:
    def __init__(self, menu):
        self.orders = {}
        self.menu = menu

    def create_order(self, order_id, table_id=None, delivery_id=None):
        if order_id not in self.orders:
            self.orders[order_id] = Order(order_id, table_id, delivery_id)
            print(f"Order {order_id} created successfully.")
        else:
            print(f"Order {order_id} already exists.")

    # def review_invoice(self):
    #     # Example of reviewing invoice
    #     total = sum(item.price * item.quantity for item in self.orders if item.order_id == self.table_id)
    #     print(f"Invoice for {self.customer_name} at table {self.table_id}: ${total}")
    #     return total
