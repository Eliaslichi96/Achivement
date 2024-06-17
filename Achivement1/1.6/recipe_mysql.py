import mysql.connector

def create_database_and_table():
    # Connect to the MySQL server
    conn = mysql.connector.connect(
        host='localhost',
        user='cf-python',
        passwd='password'
    )

    # Create a cursor object
    cursor = conn.cursor()

    # Create the database if it doesn't already exist
    cursor.execute("CREATE DATABASE IF NOT EXISTS task_database")

    # Use the new database
    cursor.execute("USE task_database")

    # Create the Recipes table if it doesn't already exist
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS Recipes (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(50),
        ingredients VARCHAR(255),
        cooking_time INT,
        difficulty VARCHAR(20)
    )
    '''
    cursor.execute(create_table_query)

    # Close the cursor and connection
    cursor.close()
    conn.close()

def main_menu(conn, cursor):
    while True:
        print("\nRecipe Management System")
        print("1. Create a new recipe")
        print("2. Search for a recipe by ingredient")
        print("3. Modify an existing recipe")
        print("4. Delete a recipe")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            create_recipe(conn, cursor)
        elif choice == '2':
            search_recipe(conn, cursor)
        elif choice == '3':
            update_recipe(conn, cursor)
        elif choice == '4':
            delete_recipe(conn, cursor)
        elif choice == '5':
            print("Exiting the Recipe Management System.")
            break
        else:
            print("Invalid choice. Please try again.")

def create_recipe(conn, cursor):
    name = input("Enter the name of the recipe: ")
    cooking_time = int(input("Enter the cooking time (in minutes): "))
    ingredients = input("Enter the ingredients (separate with comma and space): ").split(',')
    ingredients_str = ", ".join(ingredients)

    difficulty = calculate_difficulty(cooking_time, len(ingredients))

    # Insert the recipe into the database
    insert_query = '''
    INSERT INTO Recipes (name, ingredients, cooking_time, difficulty) 
    VALUES (%s, %s, %s, %s)
    '''
    cursor.execute(insert_query, (name, ingredients_str, cooking_time, difficulty))
    conn.commit()

    print("Recipe added successfully.")

def calculate_difficulty(cooking_time, num_ingredients):
    # Convert cooking_time to an integer
    cooking_time = int(cooking_time)
    
    # Calculate difficulty based on cooking_time and num_ingredients
    if cooking_time < 10 and num_ingredients < 4:
        return "Easy"
    elif cooking_time < 10 and num_ingredients >= 4:
        return "Medium"
    elif cooking_time >= 10 and num_ingredients < 4:
        return "Intermediate"
    else:
        return "Hard"

def search_recipe(conn, cursor):
    # Retrieve all ingredients from the database
    cursor.execute("SELECT ingredients FROM Recipes")
    results = cursor.fetchall()

    all_ingredients = set()
    for result in results:
        ingredients_list = result[0].split(', ')
        all_ingredients.update(ingredients_list)

    print("Available ingredients:")
    for i, ingredient in enumerate(all_ingredients, 1):
        print(f"{i}. {ingredient}")

    ingredient_index = int(input("Enter the number corresponding to the ingredient to search for: "))
    search_ingredient = list(all_ingredients)[ingredient_index - 1]

    # Search for recipes containing the specified ingredient
    search_query = '''
    SELECT * FROM Recipes 
    WHERE ingredients LIKE %s
    '''
    cursor.execute(search_query, ('%' + search_ingredient + '%',))
    results = cursor.fetchall()

    if not results:
        print("No recipes found with that ingredient.")
    else:
        print("Recipes found with that ingredient:")
        for result in results:
            print(result)

def update_recipe(conn, cursor):
    # Fetch all recipes
    cursor.execute("SELECT * FROM Recipes")
    results = cursor.fetchall()

    print("Available recipes:")
    for recipe in results:
        print(recipe)

    # Get recipe ID
    recipe_id = int(input("Enter the ID of the recipe to update: "))

    # Valid column names
    valid_columns = ['name', 'cooking_time', 'ingredients']

    # Get column name
    column_name = input("Enter the name of the column to update (name, cooking_time, ingredients): ")

    # Validate column name
    if column_name not in valid_columns:
        print(f"Error: '{column_name}' is not a valid column name.")
        return

    # Get new value
    new_value = input("Enter the new value: ")

    # Handle the case where cooking_time should be an integer
    if column_name == 'cooking_time':
        new_value = int(new_value)

    # Update query depending on column name
    if column_name == 'cooking_time' or column_name == 'ingredients':
        # Get the current value of the other column needed to calculate difficulty
        cursor.execute("SELECT cooking_time, ingredients FROM Recipes WHERE id = %s", (recipe_id,))
        current_recipe = cursor.fetchone()
        current_cooking_time = current_recipe[0]
        current_ingredients = current_recipe[1].split(', ')

        if column_name == 'cooking_time':
            new_cooking_time = new_value
            new_ingredients = current_ingredients
        else:
            new_cooking_time = current_cooking_time
            new_ingredients = new_value.split(', ')

        new_difficulty = calculate_difficulty(new_cooking_time, len(new_ingredients))

        update_query = f'''
        UPDATE Recipes 
        SET {column_name} = %s, difficulty = %s 
        WHERE id = %s
        '''
        cursor.execute(update_query, (new_value, new_difficulty, recipe_id))
    else:
        update_query = f'''
        UPDATE Recipes 
        SET {column_name} = %s 
        WHERE id = %s
        '''
        cursor.execute(update_query, (new_value, recipe_id))

    conn.commit()
    print("Recipe updated successfully.")


def delete_recipe(conn, cursor):
    # Fetch all recipes
    cursor.execute("SELECT * FROM Recipes")
    results = cursor.fetchall()

    print("Available recipes:")
    for recipe in results:
        print(recipe)

    recipe_id = int(input("Enter the ID of the recipe to delete: "))

    delete_query = "DELETE FROM Recipes WHERE id = %s"
    cursor.execute(delete_query, (recipe_id,))
    conn.commit()
    print("Recipe deleted successfully.")

def main():
    # Connect to the MySQL server
    conn = mysql.connector.connect(
        host='localhost',
        user='cf-python',
        passwd='password',
        database='task_database'
    )

    # Create a cursor object
    cursor = conn.cursor()

    # Create and connect to the database if not already done
    create_database_and_table()

    # Display the main menu
    main_menu(conn, cursor)

    # Close the cursor and connection
    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
