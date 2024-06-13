
class ShoppingList:
    def __init__(self, list_name):
        self.list_name = list_name
        self.shopping_list = []

    def add_item(self, item):
        if item not in self.shopping_list:
            self.shopping_list.append(item)
            print(f'Added {item} to the shopping list.')
        else:
            print(f'{item} is already in the shopping list.')

    def remove_item(self, item):
        if item in self.shopping_list:
            self.shopping_list.remove(item)
            print(f'Removed {item} from the shopping list.')
        else:
            print(f'{item} is not in the shopping list.')

    def view_list(self):
        print(f'{self.list_name}:')
        for item in self.shopping_list:
            print(f'- {item}')

# Create an object called pet_store_list from the ShoppingList class
pet_store_list = ShoppingList('Pet Store Shopping List')

# Add items to the list
pet_store_list.add_item('dog food')
pet_store_list.add_item('frisbee')
pet_store_list.add_item('bowl')
pet_store_list.add_item('collars')
pet_store_list.add_item('flea collars')

# Remove flea collars from the list
pet_store_list.remove_item('flea collars')

# Try adding frisbee again to the list
pet_store_list.add_item('frisbee')

# Display the entire shopping list
pet_store_list.view_list()
