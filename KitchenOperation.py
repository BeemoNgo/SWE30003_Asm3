class KitchenOperation:
    def __init__(self):
        self.order_queue = []

    def receive_order(self, order):
        self.order_queue.append(order)
        print(f"Order ID {order.order_id} received in kitchen.")

    def update_order_item_status(self, order_id, item_id, status):
        order = next((ord for ord in self.order_queue if ord.order_id == order_id), None)
        if order:
            item = next((itm for itm in order.items if itm.item_id == item_id), None)
            if item:
                item.status = status
                print(f"Status for Item ID {item_id} in Order ID {order_id} updated to {status}.")
            else:
                print("Item ID not found.")
        else:
            print("Order ID not found.")
