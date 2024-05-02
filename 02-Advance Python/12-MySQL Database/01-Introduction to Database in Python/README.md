# Introduction to Database in Python

In Python, databases are used to store and manage structured data efficiently. They are essential for many applications, from simple data storage to complex web applications. Python provides several libraries for interacting with databases, each with its own advantages and use cases. Some popular database libraries for Python include SQLite, MySQL, PostgreSQL, and MongoDB.

## SQLite:
SQLite is a lightweight, file-based relational database engine that is included as a standard library in Python. It's well-suited for smaller projects or applications that require a simple, self-contained database solution.

```python
import sqlite3

# Connect to a SQLite database (creates a new database if not exists)
conn = sqlite3.connect('example.db')

# Create a cursor object
cursor = conn.cursor()

# Execute SQL queries
cursor.execute('''CREATE TABLE IF NOT EXISTS users 
                  (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')
cursor.execute('''INSERT INTO users (name, age) VALUES (?, ?)''', ('Alice', 30))

# Commit changes and close the connection
conn.commit()
conn.close()
```

## MySQL / PostgreSQL:
For larger applications or projects requiring more advanced features, you can use libraries like mysql-connector-python for MySQL or psycopg2 for PostgreSQL. These libraries allow you to connect to MySQL or PostgreSQL databases and execute SQL queries.

```python
import mysql.connector

# Connect to a MySQL database
conn = mysql.connector.connect(
    host='localhost',
    user='username',
    password='password',
    database='database_name'
)

# Create a cursor object
cursor = conn.cursor()

# Execute SQL queries
cursor.execute('''CREATE TABLE IF NOT EXISTS users 
                  (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT)''')
cursor.execute('''INSERT INTO users (name, age) VALUES (%s, %s)''', ('Bob', 25))

# Commit changes and close the connection
conn.commit()
conn.close()
```

## MongoDB:
For NoSQL databases, MongoDB is a popular choice. You can use the pymongo library to connect to a MongoDB database and perform operations.

```python
import pymongo

# Connect to a MongoDB database
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['testdb']

# Insert documents into a collection
users_collection = db['users']
users_collection.insert_one({'name': 'Charlie', 'age': 35})
```

These examples provide a basic introduction to working with databases in Python. Depending on your project requirements and preferences, you can choose the appropriate database solution and library for your application. Each database library provides various features and functionalities, so it's essential to explore the documentation to understand how to use them effectively.