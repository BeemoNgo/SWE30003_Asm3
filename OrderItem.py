import datetime
# from KitchenOperation import KitchenOperation

class OrderItem:
    def __init__(self, order_id, quantity, description, price, type_of_order, special_request=""):
        self.order_id = order_id
        self.quantity = quantity
        self.type_of_order = type_of_order #Dine-in or delivery
        self.description = description
        self.price = price
        self.special_request = special_request
        self.order_time = datetime.datetime.now()
        self.status = 'pending'  # could be 'pending', 'preparing', 'served'

    def get_total_price(self):
        item = self.menu.get_item(self.item_id)
        if item:
            return self.quantity * self.price
        return 0
    
    def update_status(self, new_status):
        self.status = new_status
        print(f"Status of {self.description} updated to {new_status}.")

    def add_special_request(self, request):
        self.special_request = request
        print(f"Special request added to {self.description}: {request}")