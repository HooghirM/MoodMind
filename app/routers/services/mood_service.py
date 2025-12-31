import sqlite3
import datetime
from services.entry_service import get_entry_by_id

# Store an analysis result for an entry
def create_mood_score(entry_id, score, label):

    # Verify entry exists
    entry = get_entry_by_id(entry_id)
    if entry is None:
        return None
    
    # Connect to the SQLite database
    connection = sqlite3.connect('MoodMind.db')
    cursor = connection.cursor()

    # Enable foreign key support
    cursor.execute("""
    PRAGMA foreign_keys = ON;
    """)

    # Generate current timestamp
    analyzed_at = datetime.datetime.now()
    cursor.execute('INSERT INTO mood_scores (entry_id, score, label, analyzed_at) VALUES (?, ?, ?, ?)', 
                   (entry_id, score, label, analyzed_at))
    
    # Commit and close resources
    connection.commit()
    cursor.close()
    connection.close()
    return entry

# Retrieve mood scores for a specific entry
def get_mood_score_for_entry(entry_id):

     # Verify entry exists
    entry = get_entry_by_id(entry_id)
    if entry is None:
        return None
    
    # Connect to the SQLite database
    connection = sqlite3.connect('MoodMind.db')
    cursor = connection.cursor()

    # Enable foreign key support
    cursor.execute("""
    PRAGMA foreign_keys = ON;
    """)

     # Query mood scores by entry id
    cursor.execute(
    "SELECT * FROM mood_scores WHERE entry_id = ? ORDER BY analyzed_at DESC LIMIT 1",
    (entry_id,)
)
    
    rows = cursor.fetchone()

    if rows == None:
        cursor.close()
        connection.close()
        return None
    else:
        # Close resources
        cursor.close()
        connection.close()
        return rows