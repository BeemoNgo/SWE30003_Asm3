from Observer import Observer

class KitchenOperation(Observer):
    def __init__(self):
        self.order_queue = []

    def update(self, order, silent=False):
        for item in order.items:
            self.order_queue.append(item)
            table_or_delivery = f"Table {item.table_id}" if item.table_id else f"Delivery ID {item.delivery_id}"
            special_request = f" with special request: {item.special_request}" if item.special_request else ""
            if not silent:
                print(f"Order ID {order.order_id}\n{table_or_delivery} \n{item.quantity} x {item.description}{special_request}")

    def update_order_item_status(self, kitchen_id, new_status):
        item = next((itm for itm in self.order_queue if itm.kitchen_id == kitchen_id), None)
        if item:
            table_or_delivery = f"Table {item.table_id}" if item.table_id else f"Delivery ID {item.delivery_id}"
            item.status = new_status
            special_request = f" with special request: {item.special_request}" if item.special_request else ""
            # print(f"Status for {item.description} from {table_or_delivery}{special_request} updated to {new_status}.")
        else:
            print("Kitchen ID not found.")

    def display_all_order_statuses(self):
        print("Current order statuses in the kitchen:")
        for item in self.order_queue:
            print(f"------- {item.kitchen_id} --------")
            table_or_delivery = f"Table {item.table_id}" if item.table_id else f"Delivery ID {item.delivery_id}"
            special_request = f" with special request: {item.special_request}" if item.special_request else ""
            print(f"Order ID {item.order_id}\n{table_or_delivery} \n{item.quantity} x {item.description}{special_request} Status: {item.status}\n")
            print()


    def start_preparing(self, kitchen_id):
        self.update_order_item_status(kitchen_id, "Preparing")

    def complete_item(self, kitchen_id):
        index_to_remove, item_to_remove = next(
            ((index, itm) for index, itm in enumerate(self.order_queue) if itm.kitchen_id == kitchen_id),
            (None, None)
        )
        if index_to_remove is not None:
            self.update_order_item_status(kitchen_id, "Served")
            # Pop the item from the order_queue
            self.order_queue.pop(index_to_remove)
            print(f"Item {item_to_remove.description} from Table {item_to_remove.table_id} has been served.")
        else:
            print(f"Kitchen ID {kitchen_id} not found in the order queue.")
