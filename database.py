import sqlite3

# Connect to the database
conn = sqlite3.connect("event.db")

# Create cursor
cursor = conn.cursor()

# Create participants table
cursor.execute("""
CREATE TABLE IF NOT EXISTS participants (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    email TEXT NOT NULL
)
""")

conn.commit()

# Function to save participant
def save_participant(name, age, email):
    cursor.execute(
        "INSERT INTO participants (name, age, email) VALUES (?, ?, ?)",
        (name, age, email)
    )
    conn.commit()

# Function to view all participants
def view_participants():
    cursor.execute("SELECT * FROM participants")
    return cursor.fetchall()

# Function to close database
def close_database():
    conn.close()