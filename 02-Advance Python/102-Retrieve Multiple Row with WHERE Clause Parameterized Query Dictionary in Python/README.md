# Retrieve Multiple Row with WHERE Clause Parameterized Query Dictionary in Python

To retrieve multiple rows from a table with a WHERE clause using a parameterized query dictionary in Python, you can use a SQL SELECT statement with placeholders for parameters. Here's how you can accomplish this using MySQL as an example with the mysql-connector-python library:

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
sql_query = "SELECT * FROM users WHERE age > %(age)s"

# Parameter for the query
age_threshold = int(input("Enter the minimum age: "))

# Execute parameterized SQL query to select data
cursor.execute(sql_query, {'age': age_threshold})

# Fetch all rows of data
rows = cursor.fetchall()

# Display the fetched data
for row in rows:
    print(row)

# Close the cursor and connection
cursor.close()
connection.close()
```

In this example:

- We prompt the user to enter the minimum age for rows to be retrieved.
- We define a parameterized SQL query using a SELECT statement with a WHERE clause that specifies the condition for retrieval.
- We execute the parameterized SQL query using the execute() method, passing a dictionary with the parameter name as the key and the value to be retrieved as the value.
- We fetch all rows of data using the fetchall() method.
- We iterate over the fetched rows and print each row.
- Finally, we close the cursor and connection.

This approach ensures that user input is properly sanitized and prevents SQL injection attacks by using parameterized queries.

You can adapt this example to work with other databases by using the appropriate library and modifying the SQL queries accordingly. Adjust the SQL query and parameter to match your specific requirements.






