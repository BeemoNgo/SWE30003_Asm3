# class Customer:
#     def __init__(self, name, address=None):
#         self.name = name
#         self.address = address
#         self.orders = []

#     def place_order(self, order_management, items):
#         order = order_management.create_order(len(self.orders) + 1, self)
#         for item_id, quantity in items.items():
#             order.add_item(item_id, quantity, order_management.menu)
#         self.orders.append(order)
#         return order

#     def view_order_invoice(self, order):
#         print(f"Invoice for Order ID: {order.order_id}")
#         for item in order.items:
#             print(f"{item.menu.get_item(item.item_id)['description']}: {item.quantity} x ${item.menu.get_item(item.item_id)['price']:.2f}")
#         print(f"Total: ${order.get_total():.2f}")