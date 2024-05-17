from DineinCustomer import DineInCustomer
from OnlineCustomer import OnlineCustomer
from OrderManagement import OrderManagement
from Table import Table

class CustomerFactory:
    def get_customer(self, customer_type, menu, customer_name, kitchen):
        if customer_type == "dine_in":
            table = OrderManagement.get_next_available_table()
            if table is None:
                raise ValueError("No tables available")
            return DineInCustomer(menu, customer_name, table.table_id, kitchen)
        elif customer_type == "delivery":
            delivery_id = OrderManagement.get_next_delivery_id()
            return OnlineCustomer(menu, customer_name, delivery_id, kitchen)
        else:
            raise ValueError("Unknown customer type")
