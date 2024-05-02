import mysql.connector

# Create a connection to the MySQL database
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='admin',
    database='my_database'
)

# Create a cursor object to execute SQL queries
cursor = connection.cursor()

# Execute an SQL INSERT statement
cursor.execute("INSERT INTO users (name, age) VALUES ('Roman', 30)")

# Retrieve the ID of the last row inserted
last_row_id = cursor.lastrowid
print("ID of the last row inserted:", last_row_id)

# Close the cursor and connection
cursor.close()
connection.close()
