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

# Define SQL query for inserting data into the table with parameters
sql_query = "INSERT INTO users (name, age) VALUES (%s, %s)"

# Parameters for the query
parameters = ("Alif", 25)

# Execute parameterized SQL query to insert data
cursor.execute(sql_query, parameters)

# Commit the transaction
connection.commit()

# Close the cursor and connection
cursor.close()
connection.close()
