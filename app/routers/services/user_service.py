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

