import pickle

def take_recipe():
    # Taking the recipe details from the user
    recipe_name = input("Enter the recipe name: ")
    
    # Adding error handling for cooking time input
    while True:
        try:
            cooking_time = int(input("Enter the cooking time (in minutes): "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer value for cooking time.")
    
    ingredients = input("Enter the ingredients (comma-separated): ").split(',')
    ingredients = [ingredient.strip() for ingredient in ingredients]

    # Calculating the difficulty
    difficulty = calc_difficulty(cooking_time, ingredients)

    # Gathering recipe attributes into a dictionary
    recipe = {
        "name": recipe_name,
        "cooking_time": cooking_time,
        "ingredients": ingredients,
        "difficulty": difficulty
    }

    return recipe

def calc_difficulty(cooking_time, ingredients):
    # Determine difficulty based on cooking time and number of ingredients
    if cooking_time < 10 and len(ingredients) < 4:
        return "Easy"
    elif cooking_time < 10 and len(ingredients) >= 4:
        return "Medium"
    elif cooking_time >= 10 and len(ingredients) < 4:
        return "Intermediate"
    else:
        return "Hard"

# Main code
filename = input("Enter the filename to store recipes: ")

try:
    # Attempt to open and load the existing binary file
    with open(filename, 'rb') as file:
        data = pickle.load(file)
except FileNotFoundError:
    # If file not found, initialize a new data dictionary
    data = {
        "recipes_list": [],
        "all_ingredients": []
    }
except Exception as e:
    # Handle other exceptions similarly
    print(f"An error occurred: {e}")
    data = {
        "recipes_list": [],
        "all_ingredients": []
    }
else:
    # Close the file if it was opened
    file.close()
finally:
    # Extract the lists from the data dictionary
    recipes_list = data.get("recipes_list", [])
    all_ingredients = data.get("all_ingredients", [])

# Ask the user how many recipes they'd like to enter
num_recipes = int(input("How many recipes would you like to enter? "))

for _ in range(num_recipes):
    recipe = take_recipe()
    recipes_list.append(recipe)
    for ingredient in recipe["ingredients"]:
        if ingredient not in all_ingredients:
            all_ingredients.append(ingredient)

# Update the data dictionary with new lists
data = {
    "recipes_list": recipes_list,
    "all_ingredients": all_ingredients
}

# Write the updated data to the binary file
with open(filename, 'wb') as file:
    pickle.dump(data, file)

print(f"Recipes and ingredients have been saved to {filename}.")
