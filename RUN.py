import os
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

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    clear_screen()
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
    clear_screen()
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
    clear_screen()
    print("Front Staff Register")
    while True:
        action = input("Select an option:\n1. Check table status\n2. Activate table\n3. View order status by table\n4. Process payment\n5. Go back\n")
        if action == "1":
            clear_screen()
            online_system.check_table_status()
        elif action == "2":
            table_id = int(input("Enter table ID to activate: "))
            clear_screen()
            online_system.activate_table(table_id)
        elif action == "3":
            table_id = int(input("Enter table ID to view order status: "))
            clear_screen()
            online_system.get_order_status_by_table(table_id)
        elif action == "4":
            table_id = int(input("Enter table ID to process payment: "))
            clear_screen()
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
    clear_screen()
    print("Kitchen Operation")
    kitchen.display_all_order_statuses()
    while True:
        action = input("Select an option:\n1. Start preparing an item\n2. Complete an item\n3. Display order statuses\n4. Go back\n")
        if action == "1":
            item_id = int(input("Enter item ID to start preparing: "))
            kitchen.start_preparing(item_id)
            clear_screen()
        elif action == "2":
            item_id = int(input("Enter item ID to complete: "))
            kitchen.complete_item(item_id)
            clear_screen()
        elif action == "3":
            clear_screen()
            kitchen.display_all_order_statuses()
        elif action == "4":
            staff()
            break
        else:
            print("Invalid choice. Please enter a valid option.")

def customer():
    clear_screen()
    print("Welcome to Relaxing Koala Restaurant!")
    # Ask if the customer has an existing order
    has_order = input("Do you have an existing order? (yes/no): ").strip().lower()

    if has_order == "yes":
        clear_screen()
        order_id = input("Please enter your order ID: ")
        existing_order = OrderManagement.fetch_order_by_id(order_id)
        if existing_order:
            print(f"Order {order_id} found. What would you like to do next?")
            while True:
                action = input("Options: \n1. Track Order Status\n2. View Receipt\n3. Go back\nChoose an option: ")
                if action == '1':
                    clear_screen()
                    existing_order.display_order_statuses()
                elif action == '2':
                    clear_screen()
                    existing_order.display_invoice()
                elif action == '3':
                    clear_screen()
                    main()
                    break
                else:
                    print("Invalid choice. Please select a valid option.")
        else:
            print("Order ID not found. Please check and try again.")
            customer()  # Prompt again or return to the main menu

    elif has_order == "no":
        choose_customer_type()

    else:
        print("Invalid input, please enter 'yes' or 'no'.")
        customer()  # Re-prompt the same question

def choose_customer_type():
    clear_screen()
    choice = input("Choose your service: \n1. Online\n2. Dine-in\n3. Go back\n")

    if choice == "1":
        online_customer_process()
    elif choice == "2":
        dine_in_customer_process()
    elif choice == "3":
        main()
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
        choose_customer_type()


def online_customer_process():
    clear_screen()
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
    clear_screen()
    print("Welcome to Dine-in Service")

    customer_name = input("Please enter your name: ")
    while True:
        table_id = int(input("Please enter your table ID: "))
        # Find the table with the given ID
        table = next((t for t in Table.tables if t.table_id == table_id), None)

        if table and table.status in ["available", "occupied"]:  # Proceed if the table is available or occupied
            break
        else:
            print("This table is not available for ordering. Please select a different table.")

    # Create a dine-in order for the customer
    dine_in_order = factory.get_customer("dine_in", menu, customer_name, table_id, kitchen)

    # Add or remove items from the cart
    while True:
        action = input("Enter 'A' to add item, 'R' to remove item, or '0' to finish: ").upper()
        if action == '0':
            break
        elif action == 'A':
            # Display the menu
            menu.display_menu()
            item_id = int(input("Enter item ID to add to cart: "))
            quantity = int(input(f"Enter quantity for item {item_id}: "))
            special_request = input("Any special requests? (press enter to skip): ")
            clear_screen()
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

    clear_screen()
    # Send the order to the kitchen
    dine_in_order.order.send_to_kitchen(kitchen)
    online_system.add_order(dine_in_order.order)
    print("Order successfully sent to kitchen.")

    # After sending the order to the kitchen, ask the customer if they want to view the invoice or go back to main menu
    while True:
        action = input("Select an option:\n1. Track order status\n2. View Invoice\n3. Go back to Main Menu\n")
        if action == '1':
            clear_screen()
            dine_in_order.order.display_order_statuses()
        elif action == '2':
            clear_screen()
            dine_in_order.order.display_invoice()
        elif action == '3':
            main()
            break
        else:
            print("Invalid choice. Please enter '1' to view the invoice or '2' to go back to the main menu.")

def make_reservation():
    clear_screen()
    print("Making a reservation:")
    while True:
        name = input("Please enter your name: ")
        date = input("Enter the date of your reservation (YYYY-MM-DD): ")
        time = input("Enter the time of your reservation (HH:MM): ")
        guests = int(input("Enter the number of guests: "))

        try:
            online_customer = Reservation(name, date, time, guests)
            success = online_customer.make_reservation(name, date, time, guests)
            if success:
                clear_screen()
                print("Reservation made successfully.")
            else:
                print("Failed to make reservation. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}")

        # Ask the user if they want to make another reservation or go back
        next_action = input("Would you like to make another reservation or go back? (make/back): ").strip().lower()
        if next_action == "back":
            break

    main()

def order_food_for_delivery():
    clear_screen()
    print("Ordering food for delivery:")

    customer_name = input("Enter your name, phone number, and adress: ")
    # Create a delivery order for the customer
    delivery_order = factory.get_customer("delivery", menu, customer_name, None, kitchen)

    # Add or remove items from the cart
    while True:
        action = input("Enter 'A' to add item, 'R' to remove item, or '0' to finish: ").upper()
        if action == '0':
            break
        elif action == 'A':
            # Display the menu
            menu.display_menu()
            item_id = int(input("Enter item ID to add to cart: "))
            quantity = int(input(f"Enter quantity for item {item_id}: "))
            special_request = input("Any special requests? (press enter to skip): ")
            clear_screen()
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

    clear_screen()
    # Make payment
    delivery_order.make_payment()

    # After payment, ask the customer if they want to view the invoice or go back to main menu
    while True:
        action = input("Select an option: \n1. View Receipt\n2. Track Order Status\n3. Go back to Main Menu\n")
        if action == '1':
            clear_screen()
            delivery_order.view_receipt()  # Correct method to generate and view the receipt
        elif action == '2':
            clear_screen()
            delivery_order.track_order_status()
        elif action == '3':
            main()
            break
        else:
            print("Invalid choice. Please enter '1' to view the invoice\n'2' to track order status\n'3' to go back to the main menu.")

if __name__ == "__main__":
    main()

