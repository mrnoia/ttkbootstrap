import sqlite3

# Connect to or create the database
conn = sqlite3.connect('mydatabase.db')

# Create a cursor
cursor = conn.cursor()

# Create the table
cursor.execute('''CREATE TABLE data (value INTEGER)''')

# Insert some data
for i in range(9):
    cursor.execute("INSERT INTO data (value) VALUES (?)", (i+1,))

# Commit the changes and close the connection
conn.commit()
conn.close()
