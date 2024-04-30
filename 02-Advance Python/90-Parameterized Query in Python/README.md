# Parameterized Query in Python

Parameterized queries are SQL queries in which placeholders are used for parameters and the actual parameter values are supplied later when the query is executed. Parameterized queries help prevent SQL injection attacks and make the code more readable and maintainable. Here's how you can use parameterized queries in Python with MySQL as an example using the mysql-connector-python library:

1. **Install MySQL Connector/Python:**
If you haven't already installed MySQL Connector/Python, you can install it using pip:

```
pip install mysql-connector-python
```

2. **Connect to the Database:**

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
```

Replace 'localhost', 'username', 'password', and 'database_name' with the appropriate values for your MySQL setup.

3. **Execute Parameterized Query:**

```python
# Create a cursor object to execute SQL queries
cursor = connection.cursor()

# Define SQL query with parameters
sql_query = "SELECT * FROM users WHERE age > %s AND name = %s"

# Parameters for the query
parameters = (25, "Alice")

# Execute parameterized SQL query
cursor.execute(sql_query, parameters)

# Fetch all rows of data
rows = cursor.fetchall()

# Display the fetched data
for row in rows:
    print(row)

# Close the cursor and connection
cursor.close()
connection.close()
```

## Full Example:
Putting it all together:

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

# Define SQL query with parameters
sql_query = "SELECT * FROM users WHERE age > %s AND name = %s"

# Parameters for the query
parameters = (25, "Alice")

# Execute parameterized SQL query
cursor.execute(sql_query, parameters)

# Fetch all rows of data
rows = cursor.fetchall()

# Display the fetched data
for row in rows:
    print(row)

# Close the cursor and connection
cursor.close()
connection.close()
```

In this example, %s is used as a placeholder for parameters in the SQL query. When executing the query, you pass a tuple containing the parameter values to the execute() method.

This approach is safer than directly formatting the SQL query string with input values because it helps prevent SQL injection attacks by automatically escaping special characters in the input values.

You can adapt this example to work with other databases by using the appropriate library and modifying the SQL queries accordingly. Adjust the SQL query and parameters to match your specific requirements.






