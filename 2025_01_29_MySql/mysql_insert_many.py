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
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]
cursor.executemany(sql, val)

connection.commit()

print('Datas inserted')



# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("Michelle", "Blue Village")
# cursor.execute(sql, val)

# connection.commit()

# print("1 record inserted, ID:", cursor.lastrowid)
# Don't forget to close the cursor and connection when done
cursor.close()
connection.close()