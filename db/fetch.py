import sqlite3

# Connect to a database (or create it)
conn = sqlite3.connect('mydatabase.db')

# Create a cursor
cursor = conn.cursor()

# Execute SQL commands
cursor.execute("SELECT * FROM users")

for row in cursor.fetchall():
    print(row)

# Commit and close
conn.close()