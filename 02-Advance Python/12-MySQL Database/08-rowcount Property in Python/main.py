import mysql.connector

# Create a connection to the MySQL database
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='admin',
    database='my_database'
)

# Create a cursor object to execute SQL queries
cursor = connection.cursor()

# Execute an SQL INSERT statement
cursor.execute("INSERT INTO users (name, age) VALUES ('John', 30)")

# Retrieve the number of rows affected
num_rows_affected = cursor.rowcount
print("Number of rows affected:", num_rows_affected)

# Close the cursor and connection
cursor.close()
connection.close()
