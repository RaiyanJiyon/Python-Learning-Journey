# How to fetch Data from Table using fetchall Method in Python

To fetch data from a table using the fetchall() method in Python, you'll typically use a specific database library corresponding to the type of database you're working with. Here's a general outline of how you can accomplish this using MySQL as an example with the mysql-connector-python library:

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

3. **Fetch Data from the Table:**

```python
# Create a cursor object to execute SQL queries
cursor = connection.cursor()

# Define SQL query to fetch data from the table
sql_query = "SELECT * FROM users"

# Execute SQL query to fetch data
cursor.execute(sql_query)

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

# Define SQL query to fetch data from the table
sql_query = "SELECT * FROM users"

# Execute SQL query to fetch data
cursor.execute(sql_query)

# Fetch all rows of data
rows = cursor.fetchall()

# Display the fetched data
for row in rows:
    print(row)

# Close the cursor and connection
cursor.close()
connection.close()
```

This example demonstrates how to fetch data from a table using the fetchall() method in Python using MySQL Connector/Python. You can adapt this example to work with other databases by using the appropriate library and modifying the SQL queries accordingly.