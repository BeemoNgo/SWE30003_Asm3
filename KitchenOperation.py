from Observer import Observer

class KitchenOperation(Observer):
    def __init__(self):
        self.order_queue = []

    def update(self, order):
        for item in order.items:
            self.order_queue.append(item)
            table_or_delivery = f"Table {item.table_id}" if item.table_id else f"Delivery ID {item.delivery_id}"
            special_request = f" with special request: {item.special_request}" if item.special_request else ""
            print(f"Order ID {order.order_id}\n{table_or_delivery} \n{item.quantity} x {item.description}{special_request}")

    def update_order_item_status(self, item_id, new_status):
        item = next((itm for itm in self.order_queue if itm.item_id == item_id), None)
        if item:
            # Determine if item is associated with a table or delivery
            table_or_delivery = f"Table {item.table_id}" if item.table_id else f"Delivery ID {item.delivery_id}"
            item.status = new_status
            special_request = f" with special request: {item.special_request}" if item.special_request else ""
            print(f"Status for {item.description} from {table_or_delivery}{special_request} updated to {new_status}.")
        else:
            print("Item ID not found.")

    def start_preparing(self, item_id):
        self.update_order_item_status(item_id, "Preparing")

    def complete_item(self, item_id):
        self.update_order_item_status(item_id, "Served")
        self.order_queue.pop(item_id)
