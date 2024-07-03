import sqlite3
import query

# # create test.db
# conn=sqlite3.connect('recipe.db')
# c=conn.cursor()

# c.execute("INSERT INTO Recipes VALUES (1,'西红柿炒鸡蛋','10min')")
# c.execute("SELECT * FROM Recipes")
# print(c.fetchall())

# teigd=[
#     (1,'西红柿'),
#     (2,'鸡蛋'),
#     (3,'耗油'),
#     (4,'酱油')
# ]
# c.executemany("INSERT INTO Ingredients VALUES (?,?)",teigd)
# c.execute("SELECT*FROM Ingredients")
# print(c.fetchall())

# amt=[
#     (1,1,'2个'),
#     (1,2,'2个'),
#     (1,3,'1勺'),
#     (1,4,'1勺')
# ]
# c.executemany("INSERT INTO RecipeIngredients VALUES (?,?,?)",amt)
# c.execute("SELECT*FROM RecipeIngredients")
# print(c.fetchall())

# step=[
#     (1,1,1,'把西红柿洗净切块','5min'),
#     (2,1,2,'把锅加热倒油','10s'),
#     (3,1,3,'打入鸡蛋翻炒','1.5min'),
#     (4,1,4,'倒入西红柿翻炒','2.5min'),
#     (5,1,5,'加入耗油和酱油搅拌均匀','50s')
# ]
# c.executemany("INSERT INTO CookingSteps VALUES (?,?,?,?,?)",step)
# c.execute("SELECT*FROM CookingSteps")
# print(c.fetchall())
# conn.commit()
# conn.close()

query.cook_step(1)
query.show_cusine(1)