from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Set up SQLAlchemy
engine = create_engine("mysql://cf-python:password@localhost/task_database")
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

# Define the Recipe model
class Recipe(Base):
    __tablename__ = 'final_recipes'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    ingredients = Column(String(255), nullable=False)
    cooking_time = Column(Integer, nullable=False)
    difficulty = Column(String(20), nullable=False)
    
    def __repr__(self):
        return f"<Recipe(id={self.id}, name={self.name}, difficulty={self.difficulty})>"
    
    def __str__(self):
        return f"Recipe ID: {self.id}\nName: {self.name}\nIngredients: {self.ingredients}\nCooking Time: {self.cooking_time} minutes\nDifficulty: {self.difficulty}\n"
    
    def calculate_difficulty(self):
        num_ingredients = len(self.return_ingredients_as_list())
        if self.cooking_time < 10 and num_ingredients < 4:
            self.difficulty = 'Easy'
        elif self.cooking_time < 10:
            self.difficulty = 'Medium'
        elif num_ingredients < 4:
            self.difficulty = 'Intermediate'
        else:
            self.difficulty = 'Hard'
    
    def return_ingredients_as_list(self):
        if self.ingredients:
            return self.ingredients.split(', ')
        return []

# Create the table
Base.metadata.create_all(engine)

# Function to create a new recipe
def create_recipe():
    name = input("Enter the recipe name: ")
    while len(name) > 50 or not name.isalnum():
        print("Invalid name. Please enter a valid name (up to 50 alphanumeric characters).")
        name = input("Enter the recipe name: ")
    
    ingredients = []
    num_ingredients = int(input("How many ingredients would you like to enter? "))
    for _ in range(num_ingredients):
        ingredient = input("Enter an ingredient: ")
        ingredients.append(ingredient)
    
    ingredients_str = ', '.join(ingredients)
    
    cooking_time = input("Enter the cooking time in minutes: ")
    while not cooking_time.isnumeric():
        print("Invalid cooking time. Please enter a numeric value.")
        cooking_time = input("Enter the cooking time in minutes: ")
    
    cooking_time = int(cooking_time)
    
    recipe_entry = Recipe(name=name, ingredients=ingredients_str, cooking_time=cooking_time, difficulty='')
    recipe_entry.calculate_difficulty()
    
    session.add(recipe_entry)
    session.commit()
    print("Recipe added successfully!")

# Function to view all recipes
def view_all_recipes():
    recipes = session.query(Recipe).all()
    if not recipes:
        print("No recipes found.")
        return
    
    for recipe in recipes:
        print(recipe)

# Function to search for recipes by ingredients
def search_by_ingredients():
    if session.query(Recipe).count() == 0:
        print("No recipes found.")
        return
    
    results = session.query(Recipe.ingredients).all()
    all_ingredients = set()
    for result in results:
        ingredients = result[0].split(', ')
        all_ingredients.update(ingredients)
    
    all_ingredients = list(all_ingredients)
    print("Ingredients available:")
    for i, ingredient in enumerate(all_ingredients, start=1):
        print(f"{i}. {ingredient}")
    
    selected_numbers = input("Enter the ingredient numbers separated by spaces: ").split()
    selected_ingredients = []
    for num in selected_numbers:
        if num.isnumeric() and 1 <= int(num) <= len(all_ingredients):
            selected_ingredients.append(all_ingredients[int(num) - 1])
        else:
            print("Invalid selection. Exiting search.")
            return
    
    conditions = [Recipe.ingredients.like(f"%{ingredient}%") for ingredient in selected_ingredients]
    recipes = session.query(Recipe).filter(*conditions).all()
    
    if not recipes:
        print("No recipes found with the selected ingredients.")
        return
    
    for recipe in recipes:
        print(recipe)

# Function to edit a recipe
def edit_recipe():
    if session.query(Recipe).count() == 0:
        print("No recipes found.")
        return
    
    results = session.query(Recipe.id, Recipe.name).all()
    for id_, name in results:
        print(f"{id_}. {name}")
    
    recipe_id = input("Enter the ID of the recipe to edit: ")
    if not recipe_id.isnumeric() or not session.query(Recipe).filter_by(id=int(recipe_id)).first():
        print("Invalid ID. Exiting edit.")
        return
    
    recipe_to_edit = session.query(Recipe).filter_by(id=int(recipe_id)).first()
    print("Recipe details:")
    print(f"1. Name: {recipe_to_edit.name}")
    print(f"2. Ingredients: {recipe_to_edit.ingredients}")
    print(f"3. Cooking Time: {recipe_to_edit.cooking_time}")
    
    option = input("Enter the number of the attribute to edit (1-3): ")
    if option == '1':
        new_name = input("Enter the new name: ")
        while len(new_name) > 50 or not new_name.isalnum():
            print("Invalid name. Please enter a valid name (up to 50 alphanumeric characters).")
            new_name = input("Enter the new name: ")
        recipe_to_edit.name = new_name
    elif option == '2':
        new_ingredients = []
        num_ingredients = int(input("How many new ingredients would you like to enter? "))
        for _ in range(num_ingredients):
            ingredient = input("Enter a new ingredient: ")
            new_ingredients.append(ingredient)
        recipe_to_edit.ingredients = ', '.join(new_ingredients)
    elif option == '3':
        new_cooking_time = input("Enter the new cooking time in minutes: ")
        while not new_cooking_time.isnumeric():
            print("Invalid cooking time. Please enter a numeric value.")
            new_cooking_time = input("Enter the new cooking time in minutes: ")
        recipe_to_edit.cooking_time = int(new_cooking_time)
    else:
        print("Invalid selection. Exiting edit.")
        return
    
    recipe_to_edit.calculate_difficulty()
    session.commit()
    print("Recipe updated successfully!")

# Function to delete a recipe
def delete_recipe():
    if session.query(Recipe).count() == 0:
        print("No recipes found.")
        return
    
    results = session.query(Recipe.id, Recipe.name).all()
    for id_, name in results:
        print(f"{id_}. {name}")
    
    recipe_id = input("Enter the ID of the recipe to delete: ")
    if not recipe_id.isnumeric() or not session.query(Recipe).filter_by(id=int(recipe_id)).first():
        print("Invalid ID. Exiting delete.")
        return
    
    recipe_to_delete = session.query(Recipe).filter_by(id=int(recipe_id)).first()
    confirm = input(f"Are you sure you want to delete the recipe '{recipe_to_delete.name}'? (yes/no): ")
    if confirm.lower() == 'yes':
        session.delete(recipe_to_delete)
        session.commit()
        print("Recipe deleted successfully!")
    else:
        print("Delete operation cancelled.")

# Main menu
def main_menu():
    while True:
        print("\nRecipe App Menu:")
        print("1. Create a new recipe")
        print("2. View all recipes")
        print("3. Search for recipes by ingredients")
        print("4. Edit a recipe")
        print("5. Delete a recipe")
        print("Type 'quit' to exit the application")
        
        choice = input("Enter your choice: ").lower()
        
        if choice == '1':
            create_recipe()
        elif choice == '2':
            view_all_recipes()
        elif choice == '3':
            search_by_ingredients()
        elif choice == '4':
            edit_recipe()
        elif choice == '5':
            delete_recipe()
        elif choice == 'quit':
            session.close()
            engine.dispose()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
