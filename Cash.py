from Payment import Payment

class Cash(Payment):
    def __init__(self, order):
        super().__init__(order)

    def make_payment(self, received_amount):
        if received_amount >= self.order.total_cost:
            change = received_amount - self.order.total_cost
            if self.mark_order_paid():
                print(f"Payment of ${received_amount:.2f} received. Change due: ${change:.2f}")
                return True
            else:
                print("Failed to mark the order as paid.")
                return False