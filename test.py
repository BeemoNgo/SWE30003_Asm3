from Table import Table
from Reservation import Reservation
from Menu import Menu
from Order import Order
from OrderItem import OrderItem
from DineinCustomer import DineInCustomer
from OnlineCustomer import OnlineCustomer
from OrderManagement import OrderManagement


# Initialize tables
Table.initialise_tables()

# Simulate making several reservations
for _ in range(5):  # Assume you want to simulate making 10 reservations
    name = f"Customer {_}"
    reservation = Reservation(customer_name=name, date="2023-12-25", time="18:00", guests=3)
    reservation.make_reservation(date="2023-12-25", time="18:00", guests=3)

# You can also simulate cancellations and see the reservation ID being reused:
reservation_to_cancel = Reservation(customer_name="Customer for cancellation", date="2023-12-25", time="19:00", guests=2)
reservation_to_cancel.make_reservation(date="2023-12-25", time="19:00", guests=2)
reservation_to_cancel.cancel_reservation()

menu = Menu('menu_items.json') 
john = DineInCustomer(menu, "John Doe", 10)
john.create_order(1)




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