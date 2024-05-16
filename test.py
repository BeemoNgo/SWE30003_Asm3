from Table import Table
from Reservation import Reservation
from Menu import Menu
from Order import Order
from OrderItem import OrderItem
from DineinCustomer import DineInCustomer
from OnlineCustomer import OnlineCustomer
from OrderManagement import OrderManagement
from KitchenOperation import KitchenOperation


# Initialize tables
Table.initialise_tables()

# # Simulate making several reservations
# for _ in range(5):  # Assume you want to simulate making 10 reservations
#     name = f"Customer {_}"
#     reservation = Reservation(customer_name=name, date="2023-12-25", time="18:00", guests=3)
#     reservation.make_reservation(date="2023-12-25", time="18:00", guests=3)

# reservation_to_cancel = Reservation(customer_name="Customer for cancellation", date="2023-12-25", time="19:00", guests=2)
# reservation_to_cancel.make_reservation(date="2023-12-25", time="19:00", guests=2)
# reservation_to_cancel.cancel_reservation()

menu = Menu('menu_items.json')
# menu.display_menu()
kitchen = KitchenOperation()

# Initialize the Order Management system with the menu
order_mgmt = OrderManagement(menu)

# Simulate a Dine-In Customer
customer = DineInCustomer(menu, "John Doe", table_id=10)

# Customer creates an order
order = customer.order_for_table(order_id=101)

#Attach the KitchenOperation as an observer to the order
order.attach(kitchen)


# Add items to the cart
customer.orders[101].add_item_to_cart(1, 2, menu) #item_id + quantity
customer.orders[101].add_item_to_cart(2, 1, menu)
customer.orders[101].add_item_to_cart(23, 1, menu)
customer.orders[101].add_item_to_cart(40, 5, menu)

customer.orders[101].remove_item_from_cart(40, 1)

# Send the order to the kitchen
customer.orders[101].send_to_kitchen(kitchen)

kitchen.update(order)
kitchen.start_preparing(1)
# Display the current status of all items in the order
customer.orders[101].display_order_statuses()

kitchen.complete_item(2)


# Display the invoice (simulating customer review)
customer.orders[101].display_invoice()


















# # Interactive test
# while True:
#     print("\n1: Make a reservation\n2: Order food\n3: Make payment\n4: Exit")
#     choice = input("Choose an action: ")

#     if choice == '1':
#         print("Making a reservation...")
#         # Assume reservation details are predefined for simplicity
#         print("Reservation made for John Doe at 7 PM.")
#     elif choice == '2':
#         print("Ordering food...")
#         # Displaying a simplified menu for selection
#         print("Menu: 1: Cheeseburger, 2: Veggie Burger")
#         item_id = int(input("Enter item ID to order: "))
#         quantity = int(input("Enter quantity: "))
#         order = customer.place_order(order_management, {item_id: quantity})
#         print(f"Order placed for {quantity}x {menu.get_item(item_id)['description']}")
#     elif choice == '3':
#         if customer.orders:
#             customer.make_payment(customer.orders[-1])
#         else:
#             print("No order to pay for.")
#     elif choice == '4':
#         print("Exiting...")
#         break
#     else:
#         print("Invalid choice. Please select a valid option.")
