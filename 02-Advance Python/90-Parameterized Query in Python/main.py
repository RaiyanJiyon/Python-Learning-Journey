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

# Define SQL query with parameters
sql_query = "SELECT * FROM users WHERE age > %s AND name = %s"

# Parameters for the query
parameters = (25, "Alice")

# Execute parameterized SQL query
cursor.execute(sql_query, parameters)

# Fetch all rows of data
rows = cursor.fetchall()

# Display the fetched data
for row in rows:
    print(row)

# Close the cursor and connection
cursor.close()
connection.close()
