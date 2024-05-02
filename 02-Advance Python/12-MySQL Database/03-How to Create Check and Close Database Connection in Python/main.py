import mysql.connector

# Create a connection to the MySQL database
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='admin',
    port = 3306
)

# Check if the connection is successful
if connection.is_connected():
    print("Connected to MySQL database")
else:
    print("Failed to connect to MySQL database")

# Perform database operations here...

# Close the database connection when done
connection.close()

# Check if the connection is closed
if not connection.is_connected():
    print("Connection to MySQL database is closed")
