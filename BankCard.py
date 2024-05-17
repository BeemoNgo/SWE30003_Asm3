from Payment import Payment

class BankCard(Payment):
    def make_payment(self, amount):
        if amount >= self.order.total_cost:
            print(f"Credit Card Payment of ${amount} processed successfully.")
            return self.mark_order_paid()
        else:
            print("Credit Card Payment failed: Insufficient amount.")
            return False