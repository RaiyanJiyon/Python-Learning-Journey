# How to Insert Data into Table Parameterized Query Tuple in Python

To insert data into a table using a parameterized query tuple in Python, you'll typically use a specific database library corresponding to the type of database you're working with. Here's a general outline of how you can accomplish this using MySQL as an example with the mysql-connector-python library:

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

3. **Execute Parameterized Insert Query:**

```python
# Create a cursor object to execute SQL queries
cursor = connection.cursor()

# Define SQL query for inserting data into the table with parameters
sql_query = "INSERT INTO users (name, age) VALUES (%s, %s)"

# Parameters for the query
parameters = ("Alice", 25)

# Execute parameterized SQL query to insert data
cursor.execute(sql_query, parameters)

# Commit the transaction
connection.commit()

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

# Define SQL query for inserting data into the table with parameters
sql_query = "INSERT INTO users (name, age) VALUES (%s, %s)"

# Parameters for the query
parameters = ("Alif", 25)

# Execute parameterized SQL query to insert data
cursor.execute(sql_query, parameters)

# Commit the transaction
connection.commit()

# Close the cursor and connection
cursor.close()
connection.close()
```

In this example, %s is used as a placeholder for parameters in the SQL query. When executing the query, you pass a tuple containing the parameter values to the execute() method.

This approach is safer than directly formatting the SQL query string with input values because it helps prevent SQL injection attacks by automatically escaping special characters in the input values.

You can adapt this example to work with other databases by using the appropriate library and modifying the SQL queries accordingly. Adjust the SQL query and parameters to match your specific requirements.






