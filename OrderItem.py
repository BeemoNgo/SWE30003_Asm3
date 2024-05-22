import datetime
from Menu import Menu
# from KitchenOperation import KitchenOperation

class OrderItem:
    kitchen_id_counter = 1
    def __init__(self, item_id, description, price, quantity, menu, order_id=None, table_id=None, delivery_id=None, special_request=""):
        self.item_id = item_id
        self.description = description
        self.price = float(price)
        self.quantity = int(quantity)
        self.order_id = order_id
        self.table_id = table_id
        self.delivery_id = delivery_id
        self.special_request = special_request
        self.menu = menu
        # self.order_time = datetime.now()
        self.status = None  # could be 'pending', 'preparing', 'served'
        self.kitchen_id = OrderItem.kitchen_id_counter
        OrderItem.kitchen_id_counter += 1

    def get_total_price(self):
        item = self.menu.get_item(self.item_id)
        if item:
            total = self.quantity * self.price
        return total

    def update_status(self, new_status):
        self.status = new_status
        # print(f"Status of {self.item_id} updated to {new_status}.")

    def add_special_request(self, request):
        self.special_request = request
        print(f"Special request added to {self.description}: {request}")

    def __str__(self):
        return f"{self.quantity}x {self.description} with {self.special_request if self.special_request else 'no special request'} at ${self.price} each: Total ${self.get_total_price()}"
