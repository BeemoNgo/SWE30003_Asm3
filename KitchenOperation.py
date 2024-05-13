class KitchenOperation:
    def __init__(self):
        self.order_queue = []

    def receive_order(self, order):
        for item in order.items:
            self.order_queue.append(item)
            table_or_delivery = f"Table {item.table_id}" if item.table_id else f"Delivery ID {item.delivery_id}"
            print(f"Order ID {order.order_id}\n{table_or_delivery} \n{item.quantity} x {item.description}")

    def update_order_item_status(self, item_id, new_status):
        item = next((itm for itm in self.order_queue if itm.item_id == item_id), None)
        if item:
            item.status = new_status
            print(f"Status for item {item_id.description} from {item_id} updated to {new_status}.")
        else:
            print("Item ID not found.")

    def start_preparing(self, item_id):
        self.update_order_item_status(item_id, "Preparing")

    def complete_item(self, item_id):
        self.update_order_item_status(item_id, "Served")
