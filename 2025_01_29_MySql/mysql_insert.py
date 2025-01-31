import mysql.connector

# Establishing the connection
connection = mysql.connector.connect(
    host="127.0.0.1",        # or your MySQL server address
    user="myuser",    # MySQL username
    password="password",# MySQL password
    database="TUTORIALS" # Optional, specify if you want to work with a specific DB
)

# Creating a cursor object to interact with the database
cursor = connection.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
cursor.execute(sql, val)
print('Data inserted')

connection.commit()
# Don't forget to close the cursor and connection when done
cursor.close()
connection.close()