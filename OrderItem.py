import datetime
from Menu import Menu
# from KitchenOperation import KitchenOperation

class OrderItem:
    def __init__(self, order_id, quantity, description, price, menu, special_request=""):
        self.order_id = order_id
        # self.item_id = item_id
        self.quantity = quantity
        # self.type_of_order = type_of_order #Dine-in or delivery
        self.description = description
        self.price = price
        self.special_request = special_request
        self.menu = menu  # Pass the menu object to OrderItem
        # self.order_time = datetime.now()
        self.status = None  # could be 'pending', 'preparing', 'served'

    def get_total_price(self):
        item = self.menu.get_item(self.item_id)
        if item:
            total = self.quantity * self.price
        return total
    
    def update_status(self, new_status):
        self.status = new_status
        print(f"Status of {self.order_id} updated to {new_status}.")

    def add_special_request(self, request):
        self.special_request = request
        print(f"Special request added to {self.description}: {request}")