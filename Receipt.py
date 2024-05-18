class Receipt:
    def __init__(self, order, payment_method):
        self.order_id = order.order_id
        self.items = order.items
        self.total_cost = order.total_cost
        self.customer_name = order.customer_name  # Assuming we add customer_name to Order class
        self.payment_method = payment_method

    def generate_receipt(self):
        print("------ Relaxing Koala Restaurant ----------")
        print("-------------- Receipt --------------------")
        print(f"Order ID: {self.order_id}")
        print(f"Customer Name: {self.customer_name}")
        print("Items:")
        for item in self.items:
            special_request = f" with special request: {item.special_request}" if item.special_request else ""
            print(f"{item.quantity} x {item.description} at ${item.price} each{special_request}: ${item.get_total_price()}")
        print(f"Total Cost: ${self.total_cost:.2f}")
        print(f"Payment Method: {self.payment_method}")
        print("-------------------")
