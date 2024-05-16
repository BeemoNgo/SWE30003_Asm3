from Subject import Subject
from OrderItem import OrderItem
from KitchenOperation import KitchenOperation
from Table import Table

class Order(Subject):
    def __init__(self, order_id, table_id=None, delivery_id=None):
        self.order_id = order_id
        self.table_id = table_id
        self.delivery_id = delivery_id
        self.items = []  # list of OrderItem
        self.cart = [] #list of OrderItem before sending into the kitchen
        self.total_cart_cost = 0.0 #total cost of order items before sending to kitchen
        self.total_cost = 0.0
        self.is_paid = False
        self.observers = []  # List to keep track of observers

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self)

    def add_item_to_cart(self, item_id, quantity, menu):
        item_info = menu.get_item(item_id)
        if item_info:
            order_item = OrderItem(item_id, item_info['description'], item_info['price'], quantity, menu, order_id = self.order_id, table_id = self.table_id, delivery_id = self.delivery_id)
            self.cart.append(order_item)
            self.total_cart_cost += order_item.get_total_price()
            self.total_cost += order_item.get_total_price()
            print(f"Added {quantity} of {item_info['description']} to cart. Cart Total: ${self.total_cart_cost:.2f}")
        else:
            print("Item not found.")

    def remove_item_from_cart(self, item_id, quantity_to_remove):
        items_to_remove = []  # List to store items to be removed if they are to be fully removed
        total_removed_cost = 0  # Cost of removed items to adjust the total cart cost

        # First, find the item and calculate the total amount to remove
        for item in self.cart:
            if item.item_id == item_id:
                if item.quantity > quantity_to_remove:
                    # Adjust the quantity of the item in the cart
                    item.quantity -= quantity_to_remove
                    total_removed_cost += item.price * quantity_to_remove
                    print(f"Removed {quantity_to_remove} of {item.description}. Remaining: {item.quantity}. Cart Total: ${self.total_cart_cost - total_removed_cost:.2f}")
                    break  # Since we only need to remove quantity from one match, we can break after adjusting
                elif item.quantity == quantity_to_remove:
                    # If the quantity matches exactly, remove the item entirely
                    items_to_remove.append(item)
                    total_removed_cost += item.get_total_price()
                    print(f"Removed all {item.quantity} of {item.description}.")
                    break  # Remove the item completely as it matches the quantity exactly
                else:
                    # If the found item has less quantity than needed, remove it entirely and continue
                    quantity_to_remove -= item.quantity
                    total_removed_cost += item.get_total_price()
                    items_to_remove.append(item)

        # Remove items from the cart
        for item in items_to_remove:
            self.cart.remove(item)

        # Update total cart cost
        self.total_cart_cost -= total_removed_cost
        self.total_cost -= total_removed_cost

    # def remove_item(self, item):
    #     if item in self.items:
    #         self.total_cost -= item.get_total_price()
    #         self.items.remove(item)
    #         print(f"Removed item {item.description} from order.")

    def send_to_kitchen(self, kitchen):
        if not self.cart:
            print("Cart is empty. Add items before sending to kitchen.")
            return
        for item in self.cart:
            item.update_status("Pending")
            self.items.append(item)  # Move item from cart to items list
        self.cart = []  # Clear the cart after sending to kitchen
        self.total_cart_cost = 0.0 # = 0 when send to the kitchen
        print("Order successfully sent to the kitchen.")
        self.notify()  # Notify observers when the order is sent to the kitchen


    def display_order_statuses(self):
        grouped_items = {} # Create a dictionary to group items by table or delivery ID
        
        for item in self.items:
            if item.table_id:
                key = f"Table {item.table_id}"
            else:
                key = f"Delivery ID {item.delivery_id}"
            
            if key not in grouped_items:
                grouped_items[key] = []
            grouped_items[key].append(item)
        
        # Display the statuses grouped by table or delivery
        for key, items in grouped_items.items():
            print(f"Statuses for {key}:")
            for item in items:
                print(f"{item.quantity} x {item.description}, Status: {item.status}")


    def display_invoice(self):
            for item in self.items:
                print(f"{item.quantity}x {item.description} with ${item.price} each: Total ${item.get_total_price()}")
            print(f"Order Total: ${self.total_cost:.2f}")

    def mark_as_paid(self):
        self.is_paid = True
        print("Order has been marked as paid.")
