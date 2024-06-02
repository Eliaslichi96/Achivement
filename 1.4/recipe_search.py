import pickle

def display_recipe(recipe):
    print(f"Recipe Name: {recipe['name']}")
    print(f"Cooking Time: {recipe['cooking_time']} minutes")
    print(f"Ingredients: {', '.join(recipe['ingredients'])}")
    print(f"Difficulty: {recipe['difficulty']}")
    print('-' * 40)

def search_ingredient(data):
    # Display all available ingredients with their indices
    print("Available Ingredients:")
    for index, ingredient in enumerate(data["all_ingredients"], start=1):
        print(f"{index}. {ingredient}")

    # Try block to get user input and find the ingredient
    try:
        choice = int(input("\nEnter the number corresponding to the ingredient you want to search for: "))
        ingredient_searched = data["all_ingredients"][choice - 1]
    except (ValueError, IndexError):
        print("Invalid input! Please enter a valid number from the list.")
    else:
        print(f"\nRecipes containing '{ingredient_searched}':")
        for recipe in data["recipes_list"]:
            if ingredient_searched in recipe["ingredients"]:
                display_recipe(recipe)

# Main code
filename = input("Enter the filename that contains your recipe data: ")

try:
    # Attempt to open and load the binary file
    with open(filename, 'rb') as file:
        data = pickle.load(file)
except FileNotFoundError:
    print("File not found! Please ensure the filename is correct and try again.")
except Exception as e:
    print(f"An error occurred: {e}")
else:
    # Call search_ingredient function with loaded data
    search_ingredient(data)
