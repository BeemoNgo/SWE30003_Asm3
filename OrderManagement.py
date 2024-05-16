from Table import Table
from Order import Order
from OrderItem import OrderItem

class OrderManagement:
    next_delivery_id = 1  # Starting ID for deliveries
    next_order_id = 100  # Starting order ID for keeping track of orders uniquely

    def __init__(self, menu):
        self.orders = {}
        self.menu = menu

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

    def create_order(self, customer_type, customer_name):
        order_id = self.generate_next_order_id()  # Generate the next order ID
        if customer_type == "dine_in":
            table = self.get_next_available_table()
            if not table:
                print("No available tables.")
                return None
            self.orders[order_id] = Order(order_id, table_id=table.table_id)
            table.set_occupy_table()  # Mark the table as occupied
        elif customer_type == "delivery":
            delivery_id = self.get_next_delivery_id()
            self.orders[order_id] = Order(order_id, delivery_id=delivery_id)
        print(f"Order {order_id} created successfully.")
        return self.orders[order_id]

    def generate_next_order_id(self):
        self.__class__.next_order_id += 1  # Increment the class variable for order ID
        return self.__class__.next_order_id - 1
