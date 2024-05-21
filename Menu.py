import json
from tabulate import tabulate

class Menu:
    def __init__(self, file_path):
        self.items = {}
        self.load_items(file_path)

    def load_items(self, file_path):
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                for item in data:
                    self.items[item['item_id']] = {
                        'description': item['description'],
                        'price': item['price']
                    }
            print("Menu items loaded successfully.")
        except FileNotFoundError:
            print("File not found.")
        except json.JSONDecodeError:
            print("Error decoding JSON.")

    def get_item(self, item_id):
        return self.items.get(item_id, None) # Retrieve an item by item_id
    
    def display_menu(self):
    # Create a list to hold the rows of the table
        table_rows = []

        if self.items:  # Check if there are items in the menu
            # Append a header row to the table
            table_rows.append(["Item ID", "Description", "Price ($)"])
            
            # Append each menu item to the table as a row
            for item_id, details in self.items.items():
                table_rows.append([item_id, details['description'], "$"+ str(details['price'])])

            # Print the table using tabulate
            print(tabulate(table_rows, headers="firstrow", tablefmt="grid"))
        else:
            print("No items available in the menu.")


# # Example usage
# menu = Menu('menu_items.json')
# item = menu.get_item(1)
# if item:
#     print(f"Item ID: 1, Description: {item['description']}, Price: ${item['price']}")
# else:
#     print("Item not found.")

# menu.display_menu()
