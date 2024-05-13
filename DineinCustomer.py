from OrderManagement import OrderManagement
from Order import Order

class DineInCustomer(OrderManagement):
    def __init__(self, menu, customer_name, table_id):
        super().__init__(menu)
        self.customer_name = customer_name
        self.table_id = table_id

    def order_for_table(self, order_id):
        self.create_order(order_id, table_id=self.table_id)

    def provide_feedback(self, feedback):
        print(f"Feedback from {self.customer_name}: {feedback}")