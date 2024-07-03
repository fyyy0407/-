# create db to store user information
import sqlite3
conn1=sqlite3.connect('user.db')
c1=conn1.cursor()

# c1.execute("""CREATE TABLE user(
#          userID text,
#          password text
# )""")

# function to add user information
def add_user(userID, password):
    import sqlite3   
    # Connect to the database
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    
    # Check if the userID already exists
    c.execute("SELECT * FROM user WHERE userID = ?", (userID,))
    if c.fetchone():
        # UserID already exists
        print('UserID already exists, please try again.')
    else:
        # UserID does not exist, add new user
        c.execute("INSERT INTO user VALUES (?, ?)", (userID, password))
        conn.commit()
        print('Registered successfully.')
    
    # Close the connection
    conn.close()




def remove_user(userID):
    import sqlite3   
    # Connect to the database
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    
    # Check if the userID already exists
    c.execute("SELECT password FROM user WHERE userID = ?", (userID,))
    result = c.fetchone()
    if result is None:
        # UserID does not exist
        print('UserID not found, please try again.')
        return  # Exit the function if user does not exist
    else:
        # Ask for the user's password
        input_password = input(f"Please enter the password for {userID}: ")
        
        # Check if the entered password matches the stored password
        if input_password == result[0]:
            # Password is correct, delete the user
            c.execute("DELETE FROM user WHERE userID = ?", (userID,))
            conn.commit()
            print('User removed successfully.')
        else:
            # Password is incorrect
            print('Incorrect password, operation cancelled.')  
    # Close the connection
    conn.close()
