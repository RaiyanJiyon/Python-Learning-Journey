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

# Define SQL query for updating data in the table with parameters
sql_query = "UPDATE users SET age = %s WHERE name = %s"

# Parameters for the query
new_age = int(input("Enter the new age: "))
name_to_update = input("Enter the name to update: ")

# Execute parameterized SQL query to update data
cursor.execute(sql_query, (new_age, name_to_update))

# Commit the transaction
connection.commit()

# Close the cursor and connection
cursor.close()
connection.close()
