from Payment import Payment

class BankCard(Payment):
    def make_payment(self, amount):
        if amount == self.order.total_cost:
            print(f"Credit Card Payment of ${amount:.2f} processed successfully.")
            return self.mark_order_paid()
        else:
            print(f"Credit Card Payment failed: Amount provided (${amount:.2f}) does not match exact order total (${self.order.total_cost:.2f}).")
            return False
