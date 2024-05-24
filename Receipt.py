class Receipt:
    def __init__(self, order, payment_method):
        self.order_id = order.order_id
        self.items = order.items
        self.total_cost = order.total_cost
        self.customer_name = order.customer_name
        self.payment_method = payment_method

    def generate_receipt(self):
        print("\n" + "=" * 50)
        print("Relaxing Koala Restaurant".center(50))
        print("RECEIPT".center(50))
        print("=" * 50)
        print(f"Order ID: {self.order_id}")
        print(f"Customer Name: {self.customer_name}")
        print("-" * 50)
        print(f"{'Qty':<5}{'Item':<25}{'Unit Price':>10}{'Total':>10}")
        print("-" * 50)
        for item in self.items:
            total_price = item.get_total_price()
            print(f"{item.quantity:<5}{item.description:<25}${item.price:>10,.2f}${total_price:>10,.2f}")
        print("-" * 50)
        print(f"{'Total Cost:':<10}${self.total_cost:.2f}")
        print(f"Payment Method: {self.payment_method}")
        print("=" * 50 + "\n")

