# Input from user into Table Parameterized Query Dictionary in Python

To insert data into a table based on user input using a parameterized query dictionary in Python, you can use the input() function to prompt the user for input and then construct a dictionary with the input values. Here's how you can accomplish this using MySQL as an example with the mysql-connector-python library:

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

# Prompt the user for input
name = input("Enter name: ")
age = int(input("Enter age: "))  # Convert input to integer if needed

# Define SQL query for inserting data into the table with parameters
sql_query = "INSERT INTO users (name, age) VALUES (%(name)s, %(age)s)"

# Data to be inserted into the table (dictionary)
data = {
    'name': name,
    'age': age
}

# Execute parameterized SQL query to insert data
cursor.execute(sql_query, data)

# Commit the transaction
connection.commit()

# Close the cursor and connection
cursor.close()
connection.close()
```

In this example:

- We use the input() function to prompt the user to enter the name and age.
- We convert the age input to an integer using int() if needed.
- We construct a dictionary data with the user input values.
- We execute the parameterized SQL query to insert the data into the table.
- Finally, we commit the transaction and close the cursor and connection.

This approach ensures that user input is properly sanitized and prevents SQL injection attacks by using parameterized queries.

You can adapt this example to work with other databases by using the appropriate library and modifying the SQL queries accordingly. Adjust the SQL query and data dictionary to match your specific requirements.






