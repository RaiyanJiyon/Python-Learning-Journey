# How to Delete Data from Table Parameterized Query in Python

To delete data from a table using a parameterized query in Python, you can use a SQL DELETE statement with placeholders for parameters. Here's how you can accomplish this using MySQL as an example with the mysql-connector-python library:

```python
import mysql.connector

# Create a connection to the MySQL database
connection = mysql.connector.connect(
    host='localhost',
    user='username',
    password='password',
    database='database_name'
)

# Check if the connection is successful
if connection.is_connected():
    print("Connected to MySQL database")
else:
    print("Failed to connect to MySQL database")

# Create a cursor object to execute SQL queries
cursor = connection.cursor()

# Define SQL query for deleting data from the table with parameters
sql_query = "DELETE FROM users WHERE name = %s"

# Parameter for the query
name_to_delete = input("Enter the name to delete: ")

# Execute parameterized SQL query to delete data
cursor.execute(sql_query, (name_to_delete,))

# Commit the transaction
connection.commit()

# Close the cursor and connection
cursor.close()
connection.close()
```

In this example:

- We prompt the user to enter the name of the row to be deleted.
- We define a parameterized SQL query using a DELETE statement with a WHERE clause that specifies the condition for deletion.
- We execute the parameterized SQL query using the execute() method, passing the value to be deleted as a parameter.
- Finally, we commit the transaction and close the cursor and connection.

This approach ensures that user input is properly sanitized and prevents SQL injection attacks by using parameterized queries.

You can adapt this example to work with other databases by using the appropriate library and modifying the SQL queries accordingly. Adjust the SQL query and parameter to match your specific requirements.






