import json
from Table import Table
from Reservation import Reservation
from Menu import Menu
from Order import Order
from OrderItem import OrderItem
from DineinCustomer import DineInCustomer
from OnlineCustomer import OnlineCustomer
from OrderManagement import OrderManagement
from OnlineSystem import OnlineSystem
from KitchenOperation import KitchenOperation
from tabulate import tabulate
from CustomerFactory import CustomerFactory
import random


class Restaurant:
    def __init__(self, menu_file_path):
        self.menu = Menu('menu_items.json')
        self.online_system = OnlineSystem()
        self.table = Table.initialise_tables()
        self.order_management = OrderManagement.initialise_system()
        self.kitchen = KitchenOperation()
        self.factory = CustomerFactory(self.online_system)

    def display_main_menu(self):
        print("--------Main Menu:--------")
        print()
        print("1. Make Reservation")
        print("2. Place Order")
        print("3. Create Invoice")
        print("4. Make Payment")
        print()

    def handle_main_menu(self):
        while True:
            self.display_main_menu()
            choice = input("Enter your choice: ")

            if choice == '1':
                self.make_reservation()
            elif choice == '2':
                self.place_order()
            elif choice == '3':
                self.create_invoice()
            elif choice == '4':
                self.make_payment()
            else:
                print("Invalid choice. Please try again.")

    def make_reservation(self):
        # Logic to make reservation goes here
        pass

    def add_items(self, order_id):

        # # Ask the user for the item ID and quantity
        item_id = int(input("Enter the item ID you want to order: "))
        quantity = int(input("Enter the quantity: "))
        special_req = input("Enter any special request.")

        order_id.add_item_to_cart(item_id,  quantity, special_req)


    
    def remove_items(self, order_id):
        item_id = int(input("Enter the item ID you want to remove: "))
        quantity = int(input("Enter the quantity: ")) #TO DO: handle cases where added item1 but asked to remove item2
        order_id.remove_item_from_cart(item_id, quantity)


    def place_order(self):
        
        #Logic to place order goes here
        self.menu = Menu('menu_items.json') 
        self.menu.display_menu()

        
        customer_type_input = int(input("Enter:\n 1 for Dine in \n 2 for Online\n"))
        while customer_type_input!=1 and customer_type_input!=2:
            print("Wrong selection!")
            customer_type_input = int(input("Enter:\n 1 for Dine in \n 2 for Online\n"))
        if customer_type_input==1:
            customer_type = "dine_in"
        elif customer_type_input==2:
            customer_type = "delivery"

        customer_name = input("Enter customer name: ")

        order_id = self.factory.get_customer(customer_type, self.menu, customer_name, self.kitchen)
        self.add_items(order_id)



        task = int(input("Enter your choice:\n1. Add more items\n2. Remove Items\n3. Place order\n"))

        while(task!=3):
            if task==1:
                 self.add_items(order_id)
            elif task==2:
                self.remove_items(order_id)
            else:
                print("Wrong Input!")
            task = int(input("Enter your choice:\n1. Add more items\n2. Remove Items\n3. Place order\n"))
            
        order_id.send_to_kitchen(self.kitchen)

        # for item_id in order_id.
        #self.kitchen.start_preparing(1)

        
        

        # # Add the selected item to the order's cart using OrderManagement
        # self.order_management.add_item_to_cart(order_id, item_id, quantity, self.menu)
        # print("Item added to cart successfully.")


    def create_invoice(self):
        # Logic to create invoice goes here
        pass

    def make_payment(self):
        # Logic to make payment goes here
        pass


restaurant = Restaurant("menu_items.json")
restaurant.handle_main_menu()