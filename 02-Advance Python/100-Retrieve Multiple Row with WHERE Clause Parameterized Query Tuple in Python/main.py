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
sql_query = "SELECT * FROM users WHERE age > %s"

# Parameter for the query
age_threshold = int(input("Enter the minimum age: "))

# Execute parameterized SQL query to select data
cursor.execute(sql_query, (age_threshold,))

# Fetch all rows of data
rows = cursor.fetchall()

# Display the fetched data
for row in rows:
    print(row)

# Close the cursor and connection
cursor.close()
connection.close()
