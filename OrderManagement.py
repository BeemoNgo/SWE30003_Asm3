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
            return self.orders[order_id]
        else:
            print(f"Order {order_id} already exists.")
            return self.orders[order_id]

