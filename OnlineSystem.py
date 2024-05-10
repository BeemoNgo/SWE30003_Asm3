from Reservation import Reservation
from Table import Table
from Order import Order

class OnlineSystem:
    def __init__(self, all_reservations, all_tables):
        self.reservations = all_reservations
        self.tables = all_tables
        self.orders = []

    def get_reservation_info(self, reservation_id): #Manage reservation
        reservation = self.reservations.get(reservation_id)
        if reservation:
            print(f"Reservation details: {reservation}")
        else:
            print("Reservation not found.")

    def check_table_status(self, table_id): #Manage table's status
        table = self.tables.get(table_id)
        if table:
            print(f"Table {table_id} status: {table.status}")
        else:
            print("Table not found.")

    def place_order(self, order):
        self.orders.append(order)
        print(f"Order ID {order.order_id} placed.")

    def get_total_cost(self, order_id): #Handle payment process
        order = next((ord for ord in self.orders if ord.order_id == order_id), None)
        if order:
            print(f"Total cost for Order ID {order_id}: ${order.get_total():.2f}")
        else:
            print("Order ID not found.")

    def modify_order_item(self, order_id, item_id, new_quantity):
        order = next((ord for ord in self.orders if ord.order_id == order_id), None)
        if order:
            item = next((itm for itm in order.items if itm.item_id == item_id), None)
            if item:
                item.quantity = new_quantity
                print(f"Quantity for Item ID {item_id} in Order ID {order_id} updated to {new_quantity}.")
            else:
                print("Item ID not found.")
        else:
            print("Order ID not found.")
