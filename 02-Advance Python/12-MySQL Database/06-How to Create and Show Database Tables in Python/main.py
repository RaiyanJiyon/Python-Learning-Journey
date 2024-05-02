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

# Execute SQL query to create a table
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                  id INT AUTO_INCREMENT PRIMARY KEY,
                  name VARCHAR(255),
                  age INT)''')

# Execute SQL query to show tables
cursor.execute("SHOW TABLES")
tables = cursor.fetchall()
print("Available tables:")
for table in tables:
    print(table[0])

# Close the cursor and connection
cursor.close()
connection.close()
