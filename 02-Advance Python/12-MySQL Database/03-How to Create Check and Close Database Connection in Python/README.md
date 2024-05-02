# How to Create Check and Close Database Connection in Python

To create, check, and close a database connection in Python, you'll typically use a database library specific to the database you're connecting to. Here's a general outline of how you can accomplish this using the mysql-connector-python library for MySQL as an example:

1. **Install MySQL Connector/Python:**
If you haven't already installed MySQL Connector/Python, you can install it using pip:

```
pip install mysql-connector-python
```

2. **Create a Database Connection:**

```python
import mysql.connector

# Create a connection to the MySQL database
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='password',
    database='database_name'
    port = 3306
)

# Check if the connection is successful
if connection.is_connected():
    print("Connected to MySQL database")
else:
    print("Failed to connect to MySQL database")
```

Replace 'localhost', 'username', 'password', and 'database_name' with the appropriate values for your MySQL setup.

3. **Close the Database Connection:**

```python
# Close the database connection when done
connection.close()

# Check if the connection is closed
if not connection.is_connected():
    print("Connection to MySQL database is closed")
```

It's important to close the database connection when you're done using it to release any resources held by the connection.

## Full Example:
Putting it all together:

```python
import mysql.connector

# Create a connection to the MySQL database
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='password',
    database='database_name'
    port = 3306
)

# Check if the connection is successful
if connection.is_connected():
    print("Connected to MySQL database")
else:
    print("Failed to connect to MySQL database")

# Perform database operations here...

# Close the database connection when done
connection.close()

# Check if the connection is closed
if not connection.is_connected():
    print("Connection to MySQL database is closed")
```

Make sure to replace 'localhost', 'username', 'password', and 'database_name' with the appropriate values for your MySQL setup.

This example demonstrates how to create, check, and close a database connection using MySQL Connector/Python. The same principles apply when using other database libraries for different databases.

