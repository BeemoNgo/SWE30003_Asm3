from Table import Table
from Order import Order
from OrderItem import OrderItem

class OrderManagement:
    next_delivery_id = 1  # Starting ID for deliveries
    next_order_id = 100  # Starting order ID for keeping track of orders uniquely

    def __init__(self, menu, online_system):
        self.orders = {}
        self.menu = menu
        self.online_system = online_system

    @staticmethod
    def initialise_system():
        Table.initialise_tables()  # Initialize tables

    @classmethod
    def get_next_available_table(cls):
        for table in Table.tables:
            if table.is_available(None, None):  # Simplified check for the example
                return table
        return None

    @classmethod
    def get_next_delivery_id(cls):
        cls.next_delivery_id += 1
        return cls.next_delivery_id - 1

    def generate_next_order_id(self):
        self.__class__.next_order_id += 1  # Increment the class variable for order ID
        return self.__class__.next_order_id - 1

    def create_order(self, customer_type, customer_name, kitchen):
        order_id = self.generate_next_order_id()  # Generate the next order ID
        if customer_type == "dine_in":
            table = self.get_next_available_table()
            if not table:
                print("No available tables.")
                return None
            order = Order(order_id, table_id=table.table_id)
            self.orders[order_id] = order
            self.online_system.orders.append(order)
            table.set_occupy_table()  # Mark the table as occupied
            order.attach(kitchen)  # Attach the kitchen observer
        elif customer_type == "delivery":
            delivery_id = self.get_next_delivery_id()
            order = Order(order_id, delivery_id=delivery_id)
            self.orders[order_id] = order
            self.online_system.orders.append(order)
            order.attach(kitchen)
        print(f"Order {order_id} created successfully.")
        return self.orders[order_id]

    def add_item_to_cart(self, item_id, quantity, special_request=""):
        self.order.add_item_to_cart(item_id, quantity, self.menu, special_request)

    def remove_item_from_cart(self, item_id, quantity_to_remove):
        self.order.remove_item_from_cart(item_id, quantity_to_remove)

    def display_order_status(self):
        self.order.display_order_statuses()

    def display_invoice(self):
        self.order.display_invoice()
