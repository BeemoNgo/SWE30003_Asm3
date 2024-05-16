from DineinCustomer import DineInCustomer
from OnlineCustomer import OnlineCustomer


class CustomerFactory:
    def get_customer(self, customer_type, menu, customer_name, table_id=None, delivery_id=None):
        if customer_type == "dine_in":
            return DineInCustomer(menu, customer_name, table_id)
        elif customer_type == "delivery":
            return OnlineCustomer(menu, customer_name, delivery_id)
        else:
            raise ValueError("Unknown customer type")
