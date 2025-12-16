import sqlite3

class creatte_user:
    connection=sqlite3.connect('app/schemas/user.py')
    cursor=connection.cursor()