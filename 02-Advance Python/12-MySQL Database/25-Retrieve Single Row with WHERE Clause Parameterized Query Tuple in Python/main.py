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

# Define SQL query for selecting data from the table with a WHERE clause
sql_query = "SELECT * FROM users WHERE name = %s"

# Parameter for the query
name_to_retrieve = input("Enter the name to retrieve: ")

# Execute parameterized SQL query to select data
cursor.execute(sql_query, (name_to_retrieve,))

# Fetch a single row of data
row = cursor.fetchone()

# Display the fetched data
if row:
    print(row)
else:
    print("No data found for the given name.")

# Close the cursor and connection
cursor.close()
connection.close()
