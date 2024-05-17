from Table import Table
from Reservation import Reservation
from OnlineSystem import OnlineSystem
from Menu import Menu
from Order import Order
from OrderItem import OrderItem
from CustomerFactory import CustomerFactory
from OrderManagement import OrderManagement
from KitchenOperation import KitchenOperation


# Initialize tables
Table.initialise_tables()

# Initialize the online system
online_system = OnlineSystem()

menu = Menu('menu_items.json')
# menu.display_menu()
kitchen = KitchenOperation()

OrderManagement.initialise_system()  # Initialize the tables and system
factory = CustomerFactory()

online_customer = factory.get_customer("delivery", menu, "Harry Jane", kitchen)
# Customer makes a reservation
online_customer.make_reservation("2024-05-25", "18:00", 2)

# Create a new dine-in order
dine_in_order = factory.get_customer("dine_in", menu, "Michael Kenny", kitchen)
# Create a new delivery order
delivey_orderr = factory.get_customer("delivery", menu, "Deli", kitchen)

# Add items to the cart
dine_in_order.add_item_to_cart(1, 2)  # item_id + quantity
dine_in_order.add_item_to_cart(2, 1)
dine_in_order.add_item_to_cart(23, 1)
dine_in_order.add_item_to_cart(40, 5)

# Remove one item from the cart
dine_in_order.remove_item_from_cart(40, 1)

# Send the order to the kitchen
dine_in_order.send_to_kitchen(kitchen)

# Simulate the kitchen preparing an item
kitchen.start_preparing(1)  # Assuming this method handles starting preparation of an item

# Display the current status of all items in the order
dine_in_order.display_order_status()

# Simulate the kitchen completing an item
kitchen.complete_item(2)  # Assuming this method marks an item as completed

# Display the invoice (simulating customer review)
dine_in_order.display_invoice()

# Staff checks the table status
online_system.check_table_status()

# Staff views the total cost of the order
# Staff accesses the customer's table to get the total price
online_system.get_order_status_by_table(2)
# online_system.display_invoice_by_table_id(2)

# # Staff processes the payment (assuming amount entered by customer is enough)
# online_system.process_payment(dine_in_customer.table_id, "credit_card", 50.0)  # Example amount


















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
