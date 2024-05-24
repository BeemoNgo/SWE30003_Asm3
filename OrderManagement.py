from Table import Table
from Order import Order
from OrderItem import OrderItem

class OrderManagement:
    next_delivery_id = 1  # Starting ID for deliveries
    next_order_id = 100  # Starting order ID for keeping track of orders uniquely
    orders_dict = {}  # variable to store all orders with order_id as the key

    def __init__(self, menu, online_system):
        self.orders = {}
        self.menu = menu
        self.online_system = online_system

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

    @classmethod
    def fetch_order_by_id(cls, order_id):
        return cls.orders_dict.get(str(order_id))


    def create_order(cls, customer_type, customer_name, kitchen):
        order_id = cls.generate_next_order_id()  # Generate the next order ID
        if customer_type == "dine_in":
            table = cls.get_next_available_table()
            if not table:
                print("No available tables.")
                return None
            order = Order(order_id, customer_name=customer_name, table_id=table.table_id)
            cls.orders_dict[str(order_id)] = order  # Add the order to the dictionary
            table.set_occupy_table()  # Mark the table as occupied
            order.attach(kitchen)  # Attach the kitchen observer
        elif customer_type == "delivery":
            delivery_id = cls.get_next_delivery_id()
            order = Order(order_id, customer_name=customer_name, delivery_id=delivery_id)
            cls.orders_dict[str(order_id)] = order  # Add the order to the dictionary
            order.attach(kitchen)
        print(f"Order {order_id} created successfully.")
        return order

    def add_item_to_cart(self, item_id, quantity, special_request=""):
        self.order.add_item_to_cart(item_id, quantity, self.menu, special_request)

    def remove_item_from_cart(self, item_id, quantity_to_remove):
        self.order.remove_item_from_cart(item_id, quantity_to_remove)

    def display_order_status(self):
        self.order.display_order_statuses()

    def display_invoice(self):
        self.order.display_invoice()
