import mysql.connector

# Create a connection to the MySQL database
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='admin',
    database='my_database'
)

# Check if the connection is successful
if connection.is_connected():
    print("Connected to MySQL database")
else:
    print("Failed to connect to MySQL database")

cursor = connection.cursor()

sql_query = "DELETE FROM users WHERE name = %s"
data = ("Raiyan",)  # Note the comma to create a tuple

cursor.execute(sql_query, data)

connection.commit()

cursor.close()
connection.close()
