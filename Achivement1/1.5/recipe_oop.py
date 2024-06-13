class Recipe:
    all_ingredients = set()

    def __init__(self, name):
        self._name = name
        self._ingredients = []
        self._cooking_time = None
        self._difficulty = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def add_ingredients(self, *ingredients):
        self._ingredients.extend(ingredients)
        self.update_all_ingredients()

    @property
    def ingredients(self):
        return self._ingredients

    @property
    def cooking_time(self):
        return self._cooking_time

    @cooking_time.setter
    def cooking_time(self, time):
        self._cooking_time = time

    def calculate_difficulty(self):
        if self._cooking_time < 10:
            if len(self._ingredients) < 4:
                self._difficulty = "Easy"
            else:
                self._difficulty = "Medium"
        else:
            if len(self._ingredients) < 4:
                self._difficulty = "Intermediate"
            else:
                self._difficulty = "Hard"

    @property
    def difficulty(self):
        if not self._difficulty:
            self.calculate_difficulty()
        return self._difficulty

    def search_ingredient(self, ingredient):
        return ingredient in self._ingredients

    def update_all_ingredients(self):
        Recipe.all_ingredients.update(self._ingredients)

    def __str__(self):
        return f"Recipe: {self._name}\nIngredients: {', '.join(self._ingredients)}\nCooking time: {self._cooking_time} minutes\nDifficulty: {self.difficulty}"


def recipe_search(data, search_term):
    print(f"Recipes containing {search_term}:")
    for recipe in data:
        if recipe.search_ingredient(search_term):
            print(recipe)


# Creating recipes
tea = Recipe("Tea")
tea.add_ingredients("Tea Leaves", "Sugar", "Water")
tea.cooking_time = 5

coffee = Recipe("Coffee")
coffee.add_ingredients("Coffee Powder", "Sugar", "Water")
coffee.cooking_time = 5

cake = Recipe("Cake")
cake.add_ingredients("Sugar", "Butter", "Eggs", "Vanilla Essence", "Flour", "Baking Powder", "Milk")
cake.cooking_time = 50

banana_smoothie = Recipe("Banana Smoothie")
banana_smoothie.add_ingredients("Bananas", "Milk", "Peanut Butter", "Sugar", "Ice Cubes")
banana_smoothie.cooking_time = 5

# Displaying recipes
recipes_list = [tea, coffee, cake, banana_smoothie]
for recipe in recipes_list:
    print(recipe)

# Searching for recipes
search_terms = ["Water", "Sugar", "Bananas"]
for term in search_terms:
    recipe_search(recipes_list, term)
