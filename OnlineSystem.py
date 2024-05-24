from Reservation import Reservation
from Table import Table
from Order import Order
from Payment import Payment
from BankCard import BankCard
from Cash import Cash
from Receipt import Receipt

class OnlineSystem:
    def __init__(self):
        self.reservations = {}
        self.tables = {table.table_id: table for table in Table.tables}
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)

    def get_reservation_info(self, reservation_id):
        reservation = self.reservations.get(reservation_id)
        if reservation:
            print(f"Reservation details: {reservation}")
        else:
            print("Reservation not found.")

    def check_table_status(self):
        print("\033[1;37;40mTable Status Overview\033[0m")  # Bold white text on black background for the header
        print("-" * 40)  # Wider separator for better visual separation
        print(f"{'Table ID':<10}{'Status':<30}")
        print("-" * 40)
        for table_id, table in self.tables.items():
            if table.status == "available":
                status_color = "\033[1;32m"  # Green for available
            elif table.status == "occupied":
                status_color = "\033[1;33m"  # Yellow for occupied
            elif table.status == "ordered":
                status_color = "\033[1;34m"  # Blue for ordered
            elif table.status == "reserved":
                status_color = "\033[1;35m"  # Magenta for reserved
            else:
                status_color = "\033[1;37m"  # White for any other status

            # Format table row with colored status
            print(f"{table_id:<10}{status_color}{table.status:<30}\033[0m")  # Reset to default after color
        print("-" * 40)


    def get_order_status_by_table(self, table_id):
        order = self.get_order_by_table(table_id)
        if order:
            order.display_order_statuses()
        else:
            print(f"No order found for Table {table_id}.")

    def activate_table(self, table_id):
        table = self.tables.get(table_id)
        if table:
            if table.status == "available" or table.status == "reserved":
                table.set_occupy_table()
                print(f"Table {table.table_id} has been activated and is now occupied.")
            else:
                print(f"Table {table.table_id} is not available for activation (Current status: {table.status}).")
        else:
            print("Table ID not found.")

    def get_order_by_table(self, table_id):
        for order in self.orders:
            if order.table_id == table_id:
                return order
        return None

    def display_invoice_by_table_id(self, table_id):
        order = self.get_order_by_table(table_id)
        if order:
            order.display_invoice()
        else:
            print(f"No order found for Table {table_id}.")

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

    def process_payment(self, table_id, payment_method, amount):
        table = self.tables.get(table_id)
        if table and table.status == "ordered":
            order = self.get_order_by_table(table_id)
            if order:
                if payment_method == "card":
                    payment = BankCard(order)
                elif payment_method == "cash":
                    payment = Cash(order)
                else:
                    print("Invalid payment method.")
                    return

                if payment.make_payment(amount):
                    table.order_paid()
                    self.generate_receipt(order, payment_method)  # Generate receipt after payment
                    print(f"Table {table_id} payment processed and table is now free.")
                else:
                    print(f"Table {table_id} payment failed.")
            else:
                print("Order not found for the table.")
        else:
            print("Table is not in 'ordered' status or not found.")

    def generate_receipt(self, order, payment_method):
        receipt = Receipt(order, payment_method)
        receipt.generate_receipt()

    def make_reservation(self, customer_name, date, time, guests):
        reservation = Reservation(customer_name, date, time, guests)
        if reservation.make_reservation(date, time, guests):
            self.reservations[reservation.reservation_id] = reservation
            return reservation.reservation_id
        return None

    def update_reservation(self, reservation_id, new_date=None, new_time=None, new_guests=None):
        reservation = self.reservations.get(reservation_id)
        if reservation:
            reservation.update_reservation(new_date, new_time, new_guests)
        else:
            print("Reservation not found.")

    def cancel_reservation(self, reservation_id):
        reservation = self.reservations.get(reservation_id)
        if reservation:
            reservation.cancel_reservation()
            del self.reservations[reservation_id]
        else:
            print("Reservation not found.")
