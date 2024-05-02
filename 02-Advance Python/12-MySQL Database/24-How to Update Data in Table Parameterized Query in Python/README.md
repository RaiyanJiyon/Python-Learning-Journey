# How to Update Data in Table Parameterized Query in Python

To update data in a table using a parameterized query in Python, you can use a SQL UPDATE statement with placeholders for parameters. Here's how you can accomplish this using MySQL as an example with the mysql-connector-python library:

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

# Define SQL query for updating data in the table with parameters
sql_query = "UPDATE users SET age = %s WHERE name = %s"

# Parameters for the query
new_age = int(input("Enter the new age: "))
name_to_update = input("Enter the name to update: ")

# Execute parameterized SQL query to update data
cursor.execute(sql_query, (new_age, name_to_update))

# Commit the transaction
connection.commit()

# Close the cursor and connection
cursor.close()
connection.close()
```

In this example:

- We prompt the user to enter the new age and the name of the row to be updated.
- We define a parameterized SQL query using an UPDATE statement with a WHERE clause that specifies the condition for updating.
- We execute the parameterized SQL query using the execute() method, passing the new age and the name to be updated as parameters.
- Finally, we commit the transaction and close the cursor and connection.
This approach ensures that user input is properly sanitized and prevents SQL injection attacks by using parameterized queries.

You can adapt this example to work with other databases by using the appropriate library and modifying the SQL queries accordingly. Adjust the SQL query and parameters to match your specific requirements.