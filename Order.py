from OrderItem import OrderItem
from Table import Table

class Order:
    def __init__(self, order_id, table_id=None, delivery_id=None):
        self.order_id = order_id
        self.table_id = table_id
        self.delivery_id = delivery_id
        self.items = []  # list of OrderItem
        self.total_cost = 0.0
        self.is_paid = False

    def add_item(self, item_id, quantity, menu):
        item_info = menu.get_item(item_id)
        if item_info:
            order_item = OrderItem(item_id, item_info['description'], item_info['price'], quantity)
            self.items.append(order_item)
            print(f"Added {quantity} of {item_info['description']} to order.")
        else:
            print("Item not found.")

    def remove_item(self, order_item):
        if order_item in self.items:
            self.total_cost -= order_item.get_total_price()
            self.items.remove(order_item)
            print(f"Removed item {order_item.description} from order.")

    def send_to_kitchen(self):
        for item in self.items:
            item.update_status("Pending")
        print("Order successfully sent into the kitchen.")

    def display_invoice(self):
            for item in self.items:
                print(f"{item.quantity}x {item.description} at ${item.price} each: Total ${item.get_total_price()}")
            print(f"Order Total: ${self.get_total()}")

    def mark_as_paid(self):
        self.is_paid = True
        print("Order has been marked as paid.")