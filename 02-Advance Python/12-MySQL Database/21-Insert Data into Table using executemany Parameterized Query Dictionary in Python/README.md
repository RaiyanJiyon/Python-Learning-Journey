# Insert Data into Table using executemany Parameterized Query Dictionary in Python

To insert multiple rows of data into a table using the executemany() method with a parameterized query dictionary in Python, you can provide a list of dictionaries where each dictionary represents a set of values for a row. Here's how you can accomplish this using MySQL as an example with the mysql-connector-python library:

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
sql_query = "INSERT INTO users (name, age) VALUES (%(name)s, %(age)s)"

# Data to be inserted into the table (list of dictionaries)
data = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 30},
    {'name': 'Charlie', 'age': 35}
]

# Execute parameterized SQL query to insert data
cursor.executemany(sql_query, data)

# Commit the transaction
connection.commit()

# Close the cursor and connection
cursor.close()
connection.close()
```

In this example, each dictionary in the data list represents a set of values for a row to be inserted into the users table. The keys in the dictionary correspond to the column names in the table.

The executemany() method executes the SQL query with each dictionary in the list, inserting multiple rows of data into the table in a single operation.

This approach is efficient for bulk inserts and helps prevent SQL injection attacks by using parameterized queries.

You can adapt this example to work with other databases by using the appropriate library and modifying the SQL queries accordingly. Adjust the SQL query and data list to match your specific requirements.

