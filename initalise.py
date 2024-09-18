import sqlite3 
 
# Connect to the database 
connection = sqlite3.connect('my_database.db') 
cursor = connection.cursor() 
 
# Create a table 
cursor.execute(''' 
CREATE TABLE IF NOT EXISTS users ( 
    id INTEGER PRIMARY KEY, 
    name TEXT NOT NULL, 
    age INTEGER NOT NULL 
) 
''') 
 
# Insert data 
cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', ('Alice', 30)) 
cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', ('Bob', 25)) 
connection.commit() 
 
# Query the database 
cursor.execute('SELECT * FROM users') 
results = cursor.fetchall() 
 
# Print results 
for row in results: 
    print(row) 
 
# Close the connection 
cursor.close() 
connection.close() 