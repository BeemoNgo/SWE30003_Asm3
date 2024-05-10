from Order import Order
from OrderItem import OrderItem

class OrderManagement:
    def __init__(self, menu):
        self.orders = {}
        self.menu = menu

    def add_item_to_order(self, order_id, item_id, quantity):
        item = self.menu.get_item(item_id)
        if item:
            self.orders.append(OrderItem(order_id, item_id, item['description'], item['price'], quantity))
            print(f"Added {quantity} of {item['description']} to order.")
        else:
            print("Item not found.")

    def review_invoice(self):
        # Example of reviewing invoice
        total = sum(item.price * item.quantity for item in self.orders if item.order_id == self.table_id)
        print(f"Invoice for {self.customer_name} at table {self.table_id}: ${total}")
        return total
