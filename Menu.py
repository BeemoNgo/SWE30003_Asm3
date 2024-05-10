import json

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
        # Correctly referring to self.items for displaying menu
        for item_id, details in self.items.items():
            print(f"Item ID: {item_id}, Description: {details['description']}, Price: ${details['price']}")

# # Example usage
# menu = Menu('menu_items.json')
# item = menu.get_item(1)
# if item:
#     print(f"Item ID: 1, Description: {item['description']}, Price: ${item['price']}")
# else:
#     print("Item not found.")

# menu.display_menu()
