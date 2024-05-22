class Receipt:
    def __init__(self, order, payment_method):
        self.order_id = order.order_id
        self.items = order.items
        self.total_cost = order.total_cost
        self.customer_name = order.customer_name  # Assuming we add customer_name to Order class
        self.payment_method = payment_method

    def generate_receipt(self):
        print("\n" + "="*40)
        print("Relaxing Koala Restaurant".center(40))
        print("RECEIPT".center(40))
        print("="*40)
        print(f"Order ID: {self.order_id}")
        print(f"Customer Name: {self.customer_name}")
        print("-"*40)
        print(f"{'Qty':<5}{'Description':<20}{'Price Each':<10}{'Total'}")
        print("-"*40)
        for item in self.items:
            total_price = item.get_total_price()
            print(f"{item.quantity:<5}{item.description:<20}${item.price:<10.2f}${total_price:.2f}")
        print("-"*40)
        print(f"{'Total Cost:':<35}${self.total_cost:.2f}")
        print(f"Payment Method: {self.payment_method}")
        print("="*40 + "\n")

