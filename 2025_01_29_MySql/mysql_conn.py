import mysql.connector

# Establishing the connection
connection = mysql.connector.connect(
    host="127.0.0.1",        # or your MySQL server address
    user="myuser",    # MySQL username
    password="password",# MySQL password
    database="my_database" # Optional, specify if you want to work with a specific DB
)

# Creating a cursor object to interact with the database
cursor = connection.cursor()

# Example query
cursor.execute("SHOW DATABASES;")
result = cursor.fetchall()
print("Connected to database:", result)

# Don't forget to close the cursor and connection when done
cursor.close()
connection.close()
