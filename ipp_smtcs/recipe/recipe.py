# The steps of each cuisine
import sqlite3
conn3=sqlite3.connect('recipe.db')
c3=conn3.cursor()

# Execute the SQL commands to create the tables
c3.executescript("""
CREATE TABLE Recipes (
    recipe_id INTEGER PRIMARY KEY AUTOINCREMENT,
    recipe_name TEXT NOT NULL,
    total_cook_time INTEGER NOT NULL
);

CREATE TABLE Ingredients (
    ingredient_id INTEGER PRIMARY KEY AUTOINCREMENT,
    ingredient_name TEXT NOT NULL
);

CREATE TABLE RecipeIngredients (
    recipe_id INTEGER,
    ingredient_id INTEGER,
    amount TEXT NOT NULL,
    FOREIGN KEY (recipe_id) REFERENCES Recipes(recipe_id),
    FOREIGN KEY (ingredient_id) REFERENCES Ingredients(ingredient_id)
);

CREATE TABLE CookingSteps (
    step_id INTEGER PRIMARY KEY AUTOINCREMENT,
    recipe_id INTEGER,
    step_number INTEGER NOT NULL,
    instruction TEXT NOT NULL,
    step_time INTEGER NOT NULL,
    FOREIGN KEY (recipe_id) REFERENCES Recipes(recipe_id)
);
""")

conn3.commit()
conn3.close()

