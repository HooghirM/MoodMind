import sqlite3


def create_user(name, email, created_at):

    # Connect to the SQLite database 
    connection=sqlite3.connect('MoodMind.db')  
    cursor=connection.cursor()

   # Enable foreign key support
    cursor.execute("""
    PRAGMA foreign_keys = ON;
    """)

    cursor.execute('INSERT INTO users (name, email, created_at) VALUES (?, ?, ?)', (name, email, created_at))

    connection.commit()
    cursor.close()
    connection.close()

def get_user_by_id(user_id):

    # Connect to the SQLite database 
    connection=sqlite3.connect('MoodMind.db')  
    cursor=connection.cursor()  

    # Enable foreign key support
    cursor.execute("""
    PRAGMA foreign_keys = ON;
    """)

    cursor.execute('select * from users where id = ?', (user_id,))
    row = cursor.fetchone()

    if row == None:
            return None
    
    cursor.close()
    connection.close()
    return row

def get_user_by_email(email):

    # Connect to the SQLite database 
    connection=sqlite3.connect('MoodMind.db')  
    cursor=connection.cursor()  

    # Enable foreign key support
    cursor.execute("""
    PRAGMA foreign_keys = ON;
    """)

    cursor.execute('select * from users where email = ?', (email,))
    row = cursor.fetchone()

    if row == None:
            return None
    
    cursor.close()
    connection.close()
    return row
    
 

    


    

