# Insert Data into Table using executemany Parameterized Query Tuple in Python

To insert multiple rows of data into a table using the executemany() method with a parameterized query tuple in Python, you can provide a list of tuples where each tuple represents a set of values for a row. Here's how you can accomplish this using MySQL as an example with the mysql-connector-python library:

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

3. **Execute Parameterized Insert Query with executemany():**

```python
# Create a cursor object to execute SQL queries
cursor = connection.cursor()

# Define SQL query for inserting data into the table with parameters
sql_query = "INSERT INTO users (name, age) VALUES (%s, %s)"

# Data to be inserted into the table (list of tuples)
data = [
    ("Alice", 25),
    ("Bob", 30),
    ("Charlie", 35)
]

# Execute parameterized SQL query to insert data
cursor.executemany(sql_query, data)

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

# Data to be inserted into the table (list of tuples)
data = [
    ("Alice", 25),
    ("Bob", 30),
    ("Charlie", 35)
]

# Execute parameterized SQL query to insert data
cursor.executemany(sql_query, data)

# Commit the transaction
connection.commit()

# Close the cursor and connection
cursor.close()
connection.close()
```

In this example, each tuple in the data list represents a set of values for a row to be inserted into the users table. The executemany() method executes the SQL query with each tuple in the list, inserting multiple rows of data into the table in a single operation.

This approach is efficient for bulk inserts and helps prevent SQL injection attacks by using parameterized queries.

You can adapt this example to work with other databases by using the appropriate library and modifying the SQL queries accordingly. Adjust the SQL query and data list to match your specific requirements.