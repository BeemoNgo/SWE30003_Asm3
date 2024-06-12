import streamlit as st
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

def main():
    st.title("Relaxing Koala Restaurant")
    choice = st.radio("You are:", ("Customer", "Staff"), key="main_choice")

    if choice == "Customer":
        customer()
    elif choice == "Staff":
        staff()

def staff():
    st.header("Staff Options")
    choice = st.radio("You are:", ("Front Staff", "Kitchen Staff", "Go back"), key="staff_choice")

    if choice == "Front Staff":
        front_staff()
    elif choice == "Kitchen Staff":
        kitchen_staff()
    elif choice == "Go back":
        main()

def front_staff():
    st.header("Front Staff Register")
    action = st.selectbox("Select an option:", ["Check table status", "Activate table", "View order status by table", "Process payment", "Go back"], key="front_staff_action")

    if action == "Check table status":
        online_system.check_table_status()
    elif action == "Activate table":
        table_id = st.number_input("Enter table ID to activate:", min_value=1, key="activate_table_id")
        online_system.activate_table(table_id)
    elif action == "View order status by table":
        table_id = st.number_input("Enter table ID to view order status:", min_value=1, key="view_order_status_table_id")
        online_system.get_order_status_by_table(table_id)
    elif action == "Process payment":
        table_id = st.number_input("Enter table ID to process payment:", min_value=1, key="process_payment_table_id")
        online_system.display_invoice_by_table_id(table_id)
        payment_method = st.selectbox("Enter payment method:", ["card", "cash"], key="payment_method")
        amount = st.number_input("Enter the amount:", min_value=0.0, key="payment_amount")
        if st.button("Process Payment"):
            online_system.process_payment(table_id, payment_method, amount)
    elif action == "Go back":
        staff()

def kitchen_staff():
    st.header("Kitchen Operation")
    kitchen.display_all_order_statuses()
    action = st.selectbox("Select an option:", ["Start preparing an item", "Complete an item", "Display order statuses", "Go back"], key="kitchen_staff_action")

    if action == "Start preparing an item":
        item_id = st.number_input("Enter item ID to start preparing:", min_value=1, key="start_preparing_item_id")
        if st.button("Start Preparing"):
            kitchen.start_preparing(item_id)
    elif action == "Complete an item":
        item_id = st.number_input("Enter item ID to complete:", min_value=1, key="complete_item_id")
        if st.button("Complete Item"):
            kitchen.complete_item(item_id)
    elif action == "Display order statuses":
        kitchen.display_all_order_statuses()
    elif action == "Go back":
        staff()

def customer():
    st.header("Welcome to Relaxing Koala Restaurant!")
    has_order = st.radio("Do you have an existing order?", ("yes", "no"), key="has_order")

    if has_order == "yes":
        order_id = st.text_input("Please enter your order ID:", key="order_id_input")
        if order_id:
            existing_order = OrderManagement.fetch_order_by_id(order_id)
            if existing_order:
                st.write(f"Order {order_id} found. What would you like to do next?")
                action = st.radio("Options:", ["Track Order Status", "View Receipt", "Go back"], key="existing_order_action")
                if action == 'Track Order Status':
                    existing_order.display_order_statuses()
                elif action == 'View Receipt':
                    existing_order.display_invoice()
                elif action == 'Go back':
                    customer()
            else:
                st.write("Order ID not found. Please check and try again.")
                customer()  # Prompt again or return to the main menu
    elif has_order == "no":
        choose_customer_type()
    else:
        st.write("Invalid input, please enter 'yes' or 'no'.")
        customer()  # Re-prompt the same question

def choose_customer_type():
    st.header("Choose your service:")
    choice = st.radio("", ["Online", "Dine-in", "Go back"], key="choose_customer_type")

    if choice == "Online":
        online_customer_process()
    elif choice == "Dine-in":
        dine_in_customer_process()
    elif choice == "Go back":
        customer()

def online_customer_process():
    st.header("Welcome to Online Service")
    choice = st.radio("Select an option:", ["Make reservation", "Order food for delivery", "Go back"], key="online_customer_process")

    if choice == "Make reservation":
        make_reservation()
    elif choice == "Order food for delivery":
        order_food_for_delivery()
    elif choice == "Go back":
        customer()

def dine_in_customer_process():
    st.header("Welcome to Dine-in Service")

    customer_name = st.text_input("Please enter your name:", key="dine_in_customer_name")
    table_id = st.number_input("Please enter your table ID:", min_value=1, key="dine_in_table_id")

    # Find the table with the given ID
    table = next((t for t in Table.tables if t.table_id == table_id), None)

    if table and table.status in ["available", "occupied"]:  # Proceed if the table is available or occupied
        dine_in_order = factory.get_customer("dine_in", menu, customer_name, table_id, kitchen)

        while True:
            action = st.radio("Enter 'A' to add item, 'R' to remove item, or '0' to finish:", ["A", "R", "0"], key="dine_in_order_action")
            if action == '0':
                break
            elif action == 'A':
                menu.display_menu()
                item_id = st.number_input("Enter item ID to add to cart:", min_value=1, key="add_item_id")
                quantity = st.number_input(f"Enter quantity for item {item_id}:", min_value=1, key="add_item_quantity")
                special_request = st.text_input("Any special requests? (press enter to skip):", key="special_request")
                dine_in_order.order.add_item_to_cart(item_id, quantity, menu, special_request)
            elif action == 'R':
                if not dine_in_order.order.cart:
                    st.write("Your cart is empty. No items to remove.")
                else:
                    item_id = st.number_input("Enter item ID to remove from cart:", min_value=1, key="remove_item_id")
                    quantity = st.number_input(f"Enter quantity to remove for item {item_id}:", min_value=1, key="remove_item_quantity")
                    dine_in_order.order.remove_item_from_cart(item_id, quantity)

        if st.button("Send Order to Kitchen"):
            dine_in_order.order.send_to_kitchen(kitchen)
            online_system.add_order(dine_in_order.order)
            st.write("Order successfully sent to kitchen.")

            action = st.radio("Select an option:", ["Track order status", "View Invoice", "Go back to Main Menu"], key="dine_in_post_order_action")
            if action == 'Track order status':
                dine_in_order.order.display_order_statuses()
            elif action == 'View Invoice':
                dine_in_order.order.display_invoice()
            elif action == 'Go back to Main Menu':
                main()
    else:
        st.write("This table is not available for ordering. Please select a different table.")

def make_reservation():
    st.header("Making a reservation:")
    name = st.text_input("Please enter your name:", key="reservation_name")
    date = st.date_input("Enter the date of your reservation:", key="reservation_date")
    time = st.time_input("Enter the time of your reservation:", key="reservation_time")
    guests = st.number_input("Enter the number of guests:", min_value=1, key="reservation_guests")

    if st.button("Make Reservation"):
        online_customer = Reservation(name, date, time, guests)
        success = online_customer.make_reservation(name, date, time, guests)
        if success:
            st.write("Reservation made successfully.")
        else:
            st.write("Failed to make reservation. Please try again.")

def order_food_for_delivery():
    st.header("Ordering food for delivery:")

    customer_name = st.text_input("Enter your name:", key="delivery_name")
    phone_number = st.text_input("Enter your phone number:", key="delivery_phone")
    address = st.text_area("Enter your address:", key="delivery_address")

    if st.button("Proceed to Order"):
        delivery_order = factory.get_customer("delivery", menu, customer_name, None, kitchen)

        while True:
            action = st.radio("Enter 'A' to add item, 'R' to remove item, or '0' to finish:", ["A", "R", "0"], key="delivery_order_action")
            if action == '0':
                break
            elif action == 'A':
                menu.display_menu()
                item_id = st.number_input("Enter item ID to add to cart:", min_value=1, key="add_delivery_item_id")
                quantity = st.number_input(f"Enter quantity for item {item_id}:", min_value=1, key="add_delivery_item_quantity")
                special_request = st.text_input("Any special requests? (press enter to skip):", key="delivery_special_request")
                delivery_order.order.add_item_to_cart(item_id, quantity, menu, special_request)
            elif action == 'R':
                if not delivery_order.order.cart:
                    st.write("Your cart is empty. No items to remove.")
                else:
                    item_id = st.number_input("Enter item ID to remove from cart:", min_value=1, key="remove_delivery_item_id")
                    quantity = st.number_input(f"Enter quantity to remove for item {item_id}:", min_value=1, key="remove_delivery_item_quantity")
                    delivery_order.order.remove_item_from_cart(item_id, quantity)

        if st.button("Make Payment"):
            delivery_order.make_payment()
            st.write("Order successfully placed.")

            action = st.radio("Select an option:", ["View Receipt", "Track Order Status", "Go back to Main Menu"], key="delivery_post_order_action")
            if action == 'View Receipt':
                delivery_order.view_receipt()
            elif action == 'Track Order Status':
                delivery_order.track_order_status()
            elif action == 'Go back to Main Menu':
                main()

if __name__ == "__main__":
    main()
