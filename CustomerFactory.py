from OrderManagement import OrderManagement
from DineinCustomer import DineInCustomer
from OnlineCustomer import OnlineCustomer
from Table import Table

class CustomerFactory:
    def __init__(self, online_system):
        self.online_system = online_system

    def get_customer(self, customer_type, menu, customer_name, table_id, kitchen):
        if customer_type == "dine_in":
            return DineInCustomer(menu, customer_name, table_id, kitchen, self.online_system)
        elif customer_type == "delivery":
            delivery_id = OrderManagement.get_next_delivery_id()
            return OnlineCustomer(menu, customer_name, delivery_id, kitchen, self.online_system)
        else:
            raise ValueError("Unknown customer type")
