# Function used for query steps for specific cuisine
def cook_step(recipe_id):
    import sqlite3
    conn2=sqlite3.connect('recipe.db')
    c2=conn2.cursor()

    # SQL query to select the steps for a specific recipe
    c2.execute("SELECT step_number, instruction, step_time FROM CookingSteps WHERE recipe_id = ? ORDER BY step_number", (recipe_id,))
    return print(c2.fetchall())

# Function for show the cuisine
def show_cusine(recipe_id):
    import sqlite3
    conn4=sqlite3.connect('recipe.db')
    c4=conn4.cursor()

    c4.execute("""SELECT Ingredients.ingredient_name, RecipeIngredients.amount FROM Ingredients 
    JOIN RecipeIngredients ON Ingredients.ingredient_id = RecipeIngredients.ingredient_id
    WHERE RecipeIngredients.recipe_id = ?;
    """, (recipe_id,))
    igd=c4.fetchall()

    c4.execute("""SELECT recipe_name,total_cook_time FROM Recipes WHERE recipe_id=?""",(recipe_id,))
    rcName=c4.fetchall()

    c4.execute("""SELECT step_number, instruction,step_time FROM CookingSteps WHERE recipe_id=?""",(recipe_id,))
    cs=c4.fetchall()
    
    # Print and return the result
    result = f"Recipe: {rcName}\nIngredients: {igd}\nCooking Steps: {cs}"
    print(result)
    return result

