import sqlite3


class Schema:
    def __init__(self):
        self.conn = sqlite3.connect('recipe_app.db')
        self.create_recipes_table()
        self.create_categories_table()
        self.create_ingredient_categories_table()
        self.create_units_table()
        self.create_ingredient_table()
        self.conn.commit()
        self.create_recipe_to_categories_table()
        self.create_ingredient_to_categories_table()

    def create_recipes_table(self):

        query = """
        CREATE TABLE IF NOT EXISTS "Recipes" (
          recipe_id INTEGER PRIMARY KEY AUTOINCREMENT,
          recipe_name TEXT,
          link TEXT,
          instructions TEXT
        );
        """

        self.conn.execute(query)

    def create_categories_table(self):

        query = """
        CREATE TABLE IF NOT EXISTS "Categories" (
          category_id INTEGER PRIMARY KEY AUTOINCREMENT,
          category_name TEXT
        );
        """

        self.conn.execute(query)

    def create_ingredient_categories_table(self):

        query = """
        CREATE TABLE IF NOT EXISTS "Ingredient_Categories" (
          ingredient_category_id INTEGER PRIMARY KEY AUTOINCREMENT,
          ingredient_category_name TEXT
        );
        """

        self.conn.execute(query)

    def create_units_table(self):

        query = """
        CREATE TABLE IF NOT EXISTS "Units" (
          unit_id INTEGER PRIMARY KEY AUTOINCREMENT,
          unit TEXT
        );
        """

        self.conn.execute(query)

    def create_ingredient_table(self):

        query = """
        CREATE TABLE IF NOT EXISTS "Ingredients" (
          ingredient_id INTEGER PRIMARY KEY AUTOINCREMENT,
          ingredient_name TEXT,
          ingredient_unit_id INTEGER,
          FOREIGN KEY(ingredient_unit_id) REFERENCES Units(unit_id) 
        );
        """

        self.conn.execute(query)

    def create_recipe_to_categories_table(self):

        query = """
        CREATE TABLE IF NOT EXISTS "Recipe_to_Categories" (
          recipe_id INTEGER,
          category_id INTEGER,
          FOREIGN KEY(category_id) REFERENCES Categories(category_id), 
          FOREIGN KEY(recipe_id) REFERENCES Recipes(recipe_id) 
        );
        """

        self.conn.execute(query)

    def create_ingredient_to_categories_table(self):

        query = """
        CREATE TABLE IF NOT EXISTS "Ingredient_to_Categories" (
          ingredient_id INTEGER,
          ingredient_category_id INTEGER,
          FOREIGN KEY(ingredient_id) REFERENCES Ingredients(ingredient_id),
          FOREIGN KEY(ingredient_category_id) REFERENCES Ingredient_Categories(ingredient_category_id) 
        );
        """

        self.conn.execute(query)