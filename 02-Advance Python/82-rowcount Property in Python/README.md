# rowcount Property in Python

The rowcount property in Python is used to determine the number of rows affected by the last SQL statement executed using a cursor object. It is primarily used in database programming to retrieve the number of rows affected by SQL operations such as INSERT, UPDATE, DELETE, or SELECT.

### Here's how you can use the rowcount property:

After executing an SQL statement with a cursor object, you can access the rowcount property to retrieve the number of rows affected.
For SELECT statements, the rowcount property returns the number of rows retrieved from the database.
For other statements like INSERT, UPDATE, and DELETE, the rowcount property returns the number of rows that were affected by the operation.
Here's an example of how you can use the rowcount property with MySQL Connector/Python:

```python
import mysql.connector

# Create a connection to the MySQL database
connection = mysql.connector.connect(
    host='localhost',
    user='username',
    password='password',
    database='database_name'
)

# Create a cursor object to execute SQL queries
cursor = connection.cursor()

# Execute an SQL INSERT statement
cursor.execute("INSERT INTO users (name, age) VALUES ('Alice', 30)")

# Retrieve the number of rows affected
num_rows_affected = cursor.rowcount
print("Number of rows affected:", num_rows_affected)

# Close the cursor and connection
cursor.close()
connection.close()

```

In this example, the rowcount property is used to retrieve the number of rows affected by the INSERT statement executed with the cursor object.

It's important to note that the rowcount property may return -1 in some cases, such as when the database does not support the rowcount feature or when using stored procedures. Therefore, you should always check the documentation of your database library for any specific behavior related to the rowcount property.







