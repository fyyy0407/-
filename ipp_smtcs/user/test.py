import user 
import sqlite3
conn1=sqlite3.connect('user.db')
c1=conn1.cursor()
user.add_user('fy','fy0407')
user.remove_user('fy')
c1.execute("SELECT*FROM user")
print(c1.fetchall())