from OrderItem import OrderItem
from Table import Table

class Order:
    def __init__(self, order_id, table_id=None, delivery_id=None):
        self.order_id = order_id
        self.table_id = table_id
        self.delivery_id = delivery_id
        self.items = []  # list of OrderItem
        self.cart = [] #list of OrderItem before sending into the kitchen
        self.total_cart_cost = 0.0 #total cost of order items before sending to kitchen
        self.total_cost = 0.0 
        self.is_paid = False

    def add_item_to_cart(self, item_id, quantity, menu):
        item_info = menu.get_item(item_id)
        if item_info:
            order_item = OrderItem(item_id, item_info['description'], item_info['price'], quantity, menu)
            self.cart.append(order_item)
            self.total_cart_cost += order_item.get_total_price()
            self.total_cost += order_item.get_total_price()
            print(f"Added {quantity} of {item_info['description']} to cart. Cart Total: ${self.total_cart_cost:.2f}")

        else:
            print("Item not found.")

    def remove_item(self, item):
        if item in self.items:
            self.total_cost -= item.get_total_price()
            self.items.remove(item)
            print(f"Removed item {item.description} from order.")

    def send_to_kitchen(self):
        if not self.cart:
            print("Cart is empty. Add items before sending to kitchen.")
            return
        for item in self.cart:
            item.update_status("Pending")
            self.items.append(item)  # Move item from cart to items list
        self.cart = []  # Clear the cart after sending to kitchen
        self.total_cart_cost = 0.0 # = 0 when send to the kitchen
        print("Order successfully sent to the kitchen.")
        
    def get_total_cost(self):
        return sum(item.get_total_price() for item in self.items)
    
    def display_invoice(self):
            for item in self.items:
                print(f"{item.quantity}x {item.description} with ${item.price} each: Total ${item.get_total_price()}")
            print(f"Order Total: ${self.total_cost}")

    def mark_as_paid(self): 
        self.is_paid = True
        print("Order has been marked as paid.")