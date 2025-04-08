import sqlite3

# Connect to a database (or create it)
conn = sqlite3.connect('mydatabase.db')

# Create a cursor
cursor = conn.cursor()

# Execute SQL commands
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER, name TEXT)")
cursor.execute("INSERT INTO users VALUES (1, 'Alice')")

# Commit and close
conn.commit()
conn.close()
