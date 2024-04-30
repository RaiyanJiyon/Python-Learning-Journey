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

# Define SQL query to fetch data from the table
sql_query = "SELECT * FROM users"

# Execute SQL query to fetch data
cursor.execute(sql_query)

# Fetch and print each row of data
row = cursor.fetchone()
while row is not None:
    print("Row of data:", row)
    row = cursor.fetchone()

# Close the cursor and connection
cursor.close()
connection.close()
