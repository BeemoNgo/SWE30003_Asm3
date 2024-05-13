class Payment:
    def __init__(self, order):
        self.order = order

    def make_payment(self, amount):
        """ This method will be overridden by subclasses for specific payment methods"""
        pass

    def mark_order_paid(self):
        if self.order.total_cost <= 0:
            print("Payment error: Total cost is not valid.")
            return False
        self.order.mark_as_paid()
        print("Payment processed successfully. Order marked as paid.")
        return True
    
