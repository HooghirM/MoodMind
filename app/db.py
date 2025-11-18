
import sqlite3

sqliteConnection = sqlite3.connect('MoodMind.db')
cursor = sqliteConnection.cursor()

# Enable foreign key support
cursor.execute("""
PRAGMA foreign_keys = ON;
""")

# Create a users table if it doesn’t exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    created_at TEXT NOT NULL
);
""")

# Create a entries table if it doesn’t exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS entries (
    id INTEGER PRIMARY KEY,
    user_id INTEGER FOREIGN KEY,
    content TEXT NOT NULL,
    created_at TEXT NOT NULL
);
""")

# Create a mood scores table if it doesn’t exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS mood_scores (
    id INTEGER PRIMARY KEY,
    user_id INTEGER FOREIGN KEY,
    score REAL NOT NULL,
    label TEXT NOT NULL,
    analyzed_at TEXT NOT NULL
);
""")

# Create a daily summary table if it doesn’t exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS daily_summary (
    id INTEGER PRIMARY KEY,
    user_id INTEGER FOREIGN KEY,
    date TEXT NOT NULL,
    average_score REAL NOT NULL,
    entry_count INTEGER NOT NULL
);
""")


# Commit changes / close connection
sqliteConnection.commit()
cursor.close()
sqliteConnection.close()