import mysql.connector

# Connect to MySQL
def connect_db():
    return mysql.connector.connect(
        host="127.0.0.1",        # or your MySQL server address
        user="myuser",    # MySQL username
        password="password",# MySQL password
        database="employee_db" # Optional, specify if you want to work with a specific DB
    )


def create_table():
    connection=connect_db()
    cursor=connection.cursor()
    cursor.execute("CREATE TABLE employees (id INT AUTO_INCREMENT PRIMARY KEY,      first_name VARCHAR(50),    last_name VARCHAR(50),    position VARCHAR(100),    salary DECIMAL(10, 2));")
    print("Employees Table created")
    cursor.close()
    connection.close()

##create_table()

def create_employee(first_name, last_name, position="Engineer", salary="50000"):
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO employees (first_name, last_name, position, salary) VALUES (%s,%s,%s,%s)",(first_name,last_name,position,salary))
    connection.commit()
    print(f"Employee {first_name} {last_name} added successfully!")
    cursor.close()
    connection.close()

# create_employee("John", "Doe", "Software Engineer", 60000.00)



def read_employee(employee_id=None):
    connection = connect_db()
    cursor = connection.cursor()
    
    if employee_id:
        cursor.execute("SELECT * FROM employees WHERE id = %s", (employee_id,))
    else:
        cursor.execute("SELECT * FROM employees")
    
    result = cursor.fetchall()
    for row in result:
        print(f"ID: {row[0]}, Name: {row[1]} {row[2]}, Position: {row[3]}, Salary: {row[4]}")
        # print(row)
    
    cursor.close()
    connection.close()

# read_employee()




def update_employee(employee_id, first_name=None, last_name=None, position=None, salary=None):
    connection = connect_db()
    cursor = connection.cursor()
    if_value=[]
    value=[]
    if first_name:
        # set_query.append("first_name=%s ",first_name)
        if_value.append("first_name=%s ")
        value.append(first_name)

    if last_name:
        # set_query.append("last_name=%s ",last_name)
        if_value.append("last_name=%s ")
        value.append(last_name)
    if position:
        if_value.append("position=%s ")
        value.append(position)
    if salary:
        if_value.append("salary=%s ")
        value.append(salary)
    query="UPDATE employees SET "+ ", ".join(if_value)+f" WHERE id={employee_id}"
    # print(query)
    cursor.execute(query,tuple(value))
    connection.commit()
    # cursor.execute("UPDATE employees SET "+query+f" WHERE id={employee_id}")
    print(f"Employee record updated : for id={employee_id}")
    cursor.close()
    connection.close()

# update_employee(1,"John","Doe",position="Software Engineer",salary=60000)




def delete_employee(employee_id):
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM employees WHERE id = %s", (employee_id,))
    connection.commit()
    print(f"Employee with ID {employee_id} deleted!")
    
    cursor.close()
    connection.close()
delete_employee(1)