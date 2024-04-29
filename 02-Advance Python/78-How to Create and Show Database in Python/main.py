import mysql.connector

# Create a connection to the MySQL server
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='admin'
)

# Check if the connection is successful
if connection.is_connected():
    print("Connected to MySQL server")
else:
    print("Failed to connect to MySQL server")

# Create a cursor object to execute SQL queries
cursor = connection.cursor()

# Execute SQL query to create a database
cursor.execute("CREATE DATABASE IF NOT EXISTS my_database")

# Check if the database is created
cursor.execute("SHOW DATABASES")
databases = cursor.fetchall()
print("Available databases:")
for db in databases:
    print(db[0])

# Close the cursor and connection
cursor.close()
connection.close()
