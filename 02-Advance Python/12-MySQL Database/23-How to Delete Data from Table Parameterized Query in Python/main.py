import mysql.connector

# Create a connection to the MySQL database
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='admin',
    database='my_database'
)

# Check if the connection is successful
if connection.is_connected():
    print("Connected to MySQL database")
else:
    print("Failed to connect to MySQL database")

# Create a cursor object to execute SQL queries
cursor = connection.cursor()

# Define SQL query for deleting data from the table with parameters
sql_query = "DELETE FROM users WHERE name = %s"

# Parameter for the query
name_to_delete = input("Enter the name to delete: ")

# Execute parameterized SQL query to delete data
cursor.execute(sql_query, (name_to_delete,))

# Commit the transaction
connection.commit()

# Close the cursor and connection
cursor.close()
connection.close()
