# Initialize empty lists
recipes_list = []
ingredients_list = []

# Define the take_recipe function
def take_recipe():
    # Take user input for recipe details
    name = input("Enter the name of the recipe: ")
    cooking_time = int(input("Enter the cooking time in minutes: "))
    ingredients = input("Enter the ingredients (comma-separated): ").split(',')
    ingredients = [ingredient.strip() for ingredient in ingredients]  # Remove leading/trailing spaces
    
    # Create a recipe dictionary
    recipe = {
        'name': name,
        'cooking_time': cooking_time,
        'ingredients': ingredients
    }
    return recipe

# Main section of the code
if __name__ == "__main__":
    # Ask the user how many recipes they want to enter
    n = int(input("How many recipes would you like to enter? "))
    
    # Loop to gather recipes
    for _ in range(n):
        # Get the recipe dictionary from the take_recipe function
        recipe = take_recipe()
        
        # Loop through the ingredients and update the ingredients_list
        for ingredient in recipe['ingredients']:
            if ingredient not in ingredients_list:
                ingredients_list.append(ingredient)
        
        # Append the recipe to the recipes_list
        recipes_list.append(recipe)
    
    # Determine the difficulty for each recipe
    for recipe in recipes_list:
        cooking_time = recipe['cooking_time']
        num_ingredients = len(recipe['ingredients'])
        
        if cooking_time < 10:
            if num_ingredients < 4:
                difficulty = 'Easy'
            else:
                difficulty = 'Medium'
        else:
            if num_ingredients < 4:
                difficulty = 'Intermediate'
            else:
                difficulty = 'Hard'
        
        # Add the difficulty to the recipe dictionary
        recipe['difficulty'] = difficulty
    
    # Print the lists (for verification purposes)
    print("Recipes List:")
    for recipe in recipes_list:
        print("\nRecipe:")
        print(f"Name: {recipe['name']}")
        print(f"Cooking Time (minutes): {recipe['cooking_time']}")
        print("Ingredients: ")
        for ingredient in recipe['ingredients']:
            print(f"  - {ingredient}")
        print(f"Difficulty: {recipe['difficulty']}")
    
    # Print all ingredients in alphabetical order
    print("\nAll Ingredients (in alphabetical order):")
    for ingredient in sorted(ingredients_list):
        print(f"- {ingredient}")
