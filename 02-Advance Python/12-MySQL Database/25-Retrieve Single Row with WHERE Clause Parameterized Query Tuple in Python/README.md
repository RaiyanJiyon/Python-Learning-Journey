# Retrieve Single Row with WHERE Clause Parameterized Query Tuple in Python

To retrieve a single row from a table with a WHERE clause using a parameterized query tuple in Python, you can use a SQL SELECT statement with placeholders for parameters. Here's how you can accomplish this using MySQL as an example with the mysql-connector-python library:

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

# Define SQL query for selecting data from the table with a WHERE clause
sql_query = "SELECT * FROM users WHERE name = %s"

# Parameter for the query
name_to_retrieve = input("Enter the name to retrieve: ")

# Execute parameterized SQL query to select data
cursor.execute(sql_query, (name_to_retrieve,))

# Fetch a single row of data
row = cursor.fetchone()

# Display the fetched data
if row:
    print(row)
else:
    print("No data found for the given name.")

# Close the cursor and connection
cursor.close()
connection.close()
```

In this example:

- We prompt the user to enter the name of the row to be retrieved.
- We define a parameterized SQL query using a SELECT statement with a WHERE clause that specifies the condition for retrieval.
- We execute the parameterized SQL query using the execute() method, passing the name to be retrieved as a parameter.
- We fetch a single row of data using the fetchone() method.
- If the row exists, we display the fetched data. Otherwise, we print a message indicating that no data was found.
- Finally, we close the cursor and connection.

This approach ensures that user input is properly sanitized and prevents SQL injection attacks by using parameterized queries.

You can adapt this example to work with other databases by using the appropriate library and modifying the SQL queries accordingly. Adjust the SQL query and parameter to match your specific requirements.