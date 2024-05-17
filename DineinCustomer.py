from OrderManagement import OrderManagement
from Order import Order

class DineInCustomer(OrderManagement):
    def __init__(self, menu, customer_name, table_id, kitchen, online_system):
        super().__init__(menu, online_system)
        self.customer_name = customer_name
        self.table_id = table_id
        self.order = self.create_order("dine_in", customer_name, kitchen)

    def send_to_kitchen(self, kitchen):
        self.order.send_to_kitchen(kitchen)

    def provide_feedback(self, feedback):
        print(f"Feedback from {self.customer_name}: {feedback}")