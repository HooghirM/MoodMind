import sqlite3
import datetime
from services.user_service import get_user_by_id


def create_entry(user_id, content):

    # Verify User exists
    user = get_user_by_id(user_id)
    if user is None:
        return None

    # Connect to the SQLite database
    connection = sqlite3.connect("MoodMind.db")
    cursor = connection.cursor()

    # Enable foreign key support
    cursor.execute("PRAGMA foreign_keys = ON;")

    # Generate current timestamps
    currenttime = datetime.datetime.now()
    cursor.execute(
        "INSERT INTO entries (user_id, content, created_at, updated_at) VALUES (?, ?, ?, ?)",
        (user_id, content, currenttime, currenttime)
    )

    # Commit and close resources
    connection.commit()
    cursor.close()
    connection.close()


def list_entries_for_user(user_id):

    # Verify User exists
    user = get_user_by_id(user_id)
    if user is None:
        return None

    # Connect to the SQLite database
    connection = sqlite3.connect("MoodMind.db")
    cursor = connection.cursor()

    # Enable foreign key support
    cursor.execute("PRAGMA foreign_keys = ON;")

    # Query entries by user id
    cursor.execute("SELECT * FROM entries WHERE user_id = ?", (user_id,))
    rows = cursor.fetchall()
    
     # Close resources

    cursor.close()
    connection.close()

    return rows