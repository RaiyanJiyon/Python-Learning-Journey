# How to Create and Show Database in Python

To create and show a database in Python, you'll typically use a specific database library corresponding to the database you're working with. Here's a general overview using MySQL as an example with the mysql-connector-python library:

1. **Install MySQL Connector/Python:**
If you haven't already installed MySQL Connector/Python, you can install it using pip:

```
pip install mysql-connector-python
```

2. **Connect to MySQL Server:**

```python
import mysql.connector

# Create a connection to the MySQL server
connection = mysql.connector.connect(
    host='localhost',
    user='username',
    password='password'
)

# Check if the connection is successful
if connection.is_connected():
    print("Connected to MySQL server")
else:
    print("Failed to connect to MySQL server")
```

Replace 'localhost', 'username', and 'password' with the appropriate values for your MySQL setup.


3. **Create a Database:**

```python
# Create a cursor object to execute SQL queries
cursor = connection.cursor()

# Execute SQL query to create a database
cursor.execute("CREATE DATABASE IF NOT EXISTS my_database")

# Check if the database is created
cursor.execute("SHOW DATABASES")
databases = cursor.fetchall()
print("Available databases:")
for db in databases:
    print(db[0])

# Close the cursor and connection
cursor.close()
connection.close()
```

## Full Example:
Putting it all together:

```python
import mysql.connector

# Create a connection to the MySQL server
connection = mysql.connector.connect(
    host='localhost',
    user='username',
    password='password'
)

# Check if the connection is successful
if connection.is_connected():
    print("Connected to MySQL server")
else:
    print("Failed to connect to MySQL server")

# Create a cursor object to execute SQL queries
cursor = connection.cursor()

# Execute SQL query to create a database
cursor.execute("CREATE DATABASE IF NOT EXISTS my_database")

# Check if the database is created
cursor.execute("SHOW DATABASES")
databases = cursor.fetchall()
print("Available databases:")
for db in databases:
    print(db[0])

# Close the cursor and connection
cursor.close()
connection.close()
```

This example demonstrates how to create and show a database in Python using MySQL Connector/Python. You can adapt this example to work with other databases by using the appropriate library and modifying the SQL queries accordingly.