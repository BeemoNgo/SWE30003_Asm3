class Receipt:
    def __init__(self, order, payment_method):
        self.order_id = order.order_id
        self.items = order.items
        self.total_cost = order.total_cost
        self.customer_name = order.customer_name
        self.payment_method = payment_method

    def generate_receipt(self):
        print("\n" + "=" * 70)
        print("Relaxing Koala Restaurant".center(70))
        print("RECEIPT".center(70))
        print("=" * 70)
        print(f"Order ID: {self.order_id}")
        print(f"Customer Name: {self.customer_name}")
        print("-" * 70)
        print(f"{'Qty':<5}{'Item':<30}{'Unit Price':<10}{'Total':<10}")
        print("-" * 70)
        for item in self.items:
            total_price = item.get_total_price()
            print(f"{item.quantity:<5}{item.description:<30}${item.price:<10.2f}${total_price:<10.2f}")
        print("-" * 70)
        print(f"{'Total Cost:':<45}${self.total_cost:.2f}")
        print(f"Payment Method: {self.payment_method}")
        print("=" * 70 + "\n")
