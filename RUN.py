import sys
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
kitchen = KitchenOperation()

OrderManagement.initialise_system()  # Initialize the tables and system
factory = CustomerFactory(online_system)

def main():
    print("Welcome to the Relaxing Koala Restaurant")
    choice = input("You are: \n1. Customer\n2. Staff\n")
    
    if choice == "1":
        customer()
    elif choice == "2":
        staff()
        pass
    else:
        print("Invalid choice. Please enter 1 or 2.")
        main()

def staff():
    choice = input("You are: \n1. Front Staff\n2. Kitchen Staff\n3. Go back\n")
    
    if choice == "1":
        front_staff()
    elif choice == "2":
        kitchen_staff()
    elif choice == "3":
        main()
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
        staff()

def front_staff():
    print("Front Staff Register")
    while True:
        action = input("Select an option:\n1. Check table status\n2. Activate table\n3. View order status by table\n4. Process payment\n5. Go back\n")
        if action == "1":
            online_system.check_table_status()
        elif action == "2":
            table_id = int(input("Enter table ID to activate: "))
            online_system.activate_table(table_id)
        elif action == "3":
            table_id = int(input("Enter table ID to view order status: "))
            online_system.get_order_status_by_table(table_id)
        elif action == "4":
            table_id = int(input("Enter table ID to process payment: "))
            online_system.display_invoice_by_table_id(table_id)
            payment_method = input("Enter payment method (card/cash): ")
            amount = float(input("Enter the amount: "))
            online_system.process_payment(table_id, payment_method, amount)
        elif action == "5":
            staff()
            break
        else:
            print("Invalid choice. Please enter a valid option.")

def kitchen_staff():
    print("Kitchen Operation")
    kitchen.display_all_order_statuses()
    while True:
        action = input("Select an option:\n1. Start preparing an item\n2. Complete an item\n3. Display order statuses\n4. Go back\n")
        if action == "1":
            item_id = int(input("Enter item ID to start preparing: "))
            kitchen.start_preparing(item_id)
        elif action == "2":
            item_id = int(input("Enter item ID to complete: "))
            kitchen.complete_item(item_id)
        elif action == "3":
            kitchen.display_all_order_statuses()
        elif action == "4":
            staff()
            break
        else:
            print("Invalid choice. Please enter a valid option.")

def customer():
    choice = input("Choose your service: \n1. Online\n2. Dine-in\n3. Go back\n")
    
    if choice == "1":
        online_customer_process()
    elif choice == "2":
        dine_in_customer_process()
    elif choice == "3":
        main()
    else:
        print("Invalid choice. Please enter 1 or 2.")
        customer()

def online_customer_process():
    print("Welcome to Online Service")
    choice = input("Select an option:\n1. Make reservation\n2. Order food for delivery\n3. Go back\n")
    
    if choice == "1":
        make_reservation()
    elif choice == "2":
        order_food_for_delivery()
    elif choice == "3":
        customer()
    else:
        print("Invalid choice. Please enter 1 or 2.")
        online_customer_process()

def dine_in_customer_process():
    print("Welcome to Dine-in Service")

    customer_name = input("Please enter your name: ")

    # Create a dine-in order for the customer
    dine_in_order = factory.get_customer("dine_in", menu, customer_name, kitchen)
    # Display the menu
    menu.display_menu()
    # Add or remove items from the cart
    while True:
        action = input("Enter 'A' to add item, 'R' to remove item, or '0' to finish: ").upper()
        if action == '0':
            break
        elif action == 'A':
            item_id = int(input("Enter item ID to add to cart: "))
            quantity = int(input(f"Enter quantity for item {item_id}: "))
            special_request = input("Any special requests? (press enter to skip): ")
            dine_in_order.order.add_item_to_cart(item_id, quantity, menu, special_request)
        elif action == 'R':
            if not dine_in_order.order.cart:
                print("Your cart is empty. No items to remove.")
            else:
                item_id = int(input("Enter item ID to remove from cart: "))
                quantity = int(input(f"Enter quantity to remove for item {item_id}: "))
                dine_in_order.order.remove_item_from_cart(item_id, quantity)
        else:
            print("Invalid choice. Please enter 'A' to add, 'R' to remove, or '0' to finish.")

    # Send the order to the kitchen
    dine_in_order.order.send_to_kitchen(kitchen)
    print("Order successfully sent to kitchen.")

    # After sending the order to the kitchen, ask the customer if they want to view the invoice or go back to main menu
    while True:
        action = input("Select an option: \n1. View Invoice\n2. Go back to Main Menu\n")
        if action == '1':
            dine_in_order.order.display_invoice()
        elif action == '2':
            main()
            break
        else:
            print("Invalid choice. Please enter '1' to view the invoice or '2' to go back to the main menu.")

def make_reservation():
    print("Making a reservation:")
    name = input("Please enter your name: ")
    date = input("Enter the date of your reservation (YYYY-MM-DD): ")
    time = input("Enter the time of your reservation (HH:MM): ")
    guests = int(input("Enter the number of guests: "))

    try:
        online_customer = Reservation(name, date, time, guests)
        success = online_customer.make_reservation(name, date, time, guests)
        if success:
            print("Reservation made successfully.")
        else:
            print("Failed to make reservation. Please try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

def order_food_for_delivery():
    print("Ordering food for delivery:")
    
    customer_name = input("Enter your name: ")
    # Create a delivery order for the customer
    delivery_order = factory.get_customer("delivery", menu, customer_name, kitchen)

    # Display the menu
    menu.display_menu()

    # Add or remove items from the cart
    while True:
        action = input("Enter 'A' to add item, 'R' to remove item, or '0' to finish: ").upper()
        if action == '0':
            break
        elif action == 'A':
            item_id = int(input("Enter item ID to add to cart: "))
            quantity = int(input(f"Enter quantity for item {item_id}: "))
            special_request = input("Any special requests? (press enter to skip): ")
            delivery_order.order.add_item_to_cart(item_id, quantity, menu, special_request)
        elif action == 'R':
            if not delivery_order.order.cart:
                print("Your cart is empty. No items to remove.")
            else:
                item_id = int(input("Enter item ID to remove from cart: "))
                quantity = int(input(f"Enter quantity to remove for item {item_id}: "))
                delivery_order.order.remove_item_from_cart(item_id, quantity)
        else:
            print("Invalid choice. Please enter 'A' to add, 'R' to remove, or '0' to finish.")

    # Make payment
    delivery_order.order.display_invoice()
    amount = float(input("Enter the amount to pay: "))
    delivery_order.make_payment(amount)

    # After payment, ask the customer if they want to view the invoice or go back to main menu
    while True:
        action = input("Select an option: \n1. View Receipt\n2. Track Order Status\n3. Go back to Main Menu\n")
        if action == '1':
            delivery_order.generate_receipt()
        elif action == '2':
            delivery_order.track_order_status()
        elif action == '3':
            main()
            break
        else:
            print("Invalid choice. Please enter '1' to view the invoice, '2' to track order status, or '3' to go back to the main menu.")

if __name__ == "__main__":
    main()

