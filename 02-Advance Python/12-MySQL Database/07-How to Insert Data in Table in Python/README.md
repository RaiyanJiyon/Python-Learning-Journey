# How to Insert Data in Table in Python

To insert data into a table in Python, you'll typically use a specific library corresponding to the type of database you're working with. Here's a general outline of how you can accomplish this using MySQL as an example with the mysql-connector-python library:

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

3. **Insert Data into the Table:**

```python
# Create a cursor object to execute SQL queries
cursor = connection.cursor()

# Define SQL query to insert data into the table
sql_query = "INSERT INTO users (name, age) VALUES (%s, %s)"

# Data to be inserted into the table
data = ("Alice", 30)

# Execute SQL query to insert data
cursor.execute(sql_query, data)

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

# Define SQL query to insert data into the table
sql_query = "INSERT INTO users (name, age) VALUES (%s, %s)"

# Data to be inserted into the table
data = ("Jiyon", 24)

# Execute SQL query to insert data
cursor.execute(sql_query, data)

# Commit the transaction
connection.commit()

# Close the cursor and connection
cursor.close()
connection.close()
```

This example demonstrates how to insert data into a table in Python using MySQL Connector/Python. You can adapt this example to work with other databases by using the appropriate library and modifying the SQL queries accordingly.