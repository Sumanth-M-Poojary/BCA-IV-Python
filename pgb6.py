# Import mysql connector package
import mysql.connector

# Connect Python with MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="studentdb2"
)

# Create cursor object
cur = conn.cursor()


# Function to add employee details
def add():

    # Get employee details from user
    eno = int(input("Enter employee number: "))
    name = input("Enter employee name: ")
    salary = int(input("Enter salary: "))

    # SQL INSERT query
    qry = "INSERT INTO employee VALUES(%s,%s,%s)"

    # Store values in tuple
    values = (eno, name, salary)

    try:
        # Execute query
        cur.execute(qry, values)

        # Save changes permanently
        conn.commit()

        print("Details saved successfully")

    # Handle duplicate primary key error
    except mysql.connector.IntegrityError:
        print("Employee already exists in database")


# Function to display employee using employee number
def display():

    # Get employee number
    eno = int(input("Enter employee number: "))

    # SQL SELECT query
    qry = "SELECT * FROM employee WHERE eno=%s"

    # Tuple value
    value = (eno,)

    # Execute query
    cur.execute(qry, value)

    # Fetch one record
    row = cur.fetchone()

    # Check whether employee exists
    if row:

        print("\nEmployee Details")
        print("EmpNo\tName\tSalary")

        # Display employee data
        print(f"{row[0]}\t{row[1]}\t{row[2]}")

    else:
        print("Employee not found")


# Function to display employees within salary range
def rangesalary():

    # Get salary range
    min_salary = int(input("Enter minimum salary: "))
    max_salary = int(input("Enter maximum salary: "))

    # SQL query using BETWEEN operator
    qry = "SELECT * FROM employee WHERE salary BETWEEN %s AND %s"

    # Store range values
    value = (min_salary, max_salary)

    # Execute query
    cur.execute(qry, value)

    # Fetch all matching records
    rows = cur.fetchall()

    # Check if records exist
    if rows:

        print("\nEmployee Details")
        print("EmpNo\tName\tSalary")

        # Display all employees
        for row in rows:
            print(f"{row[0]}\t{row[1]}\t{row[2]}")

    else:
        print("No employee found in this salary range")


# Main menu loop
while True:

    print("\n===== Employee Management System =====")
    print("1. Add Employee")
    print("2. Get Employee")
    print("3. Show Employees by Salary Range")
    print("4. Exit")

    # Get user choice
    ch = int(input("Enter your choice: "))

    # Call add function
    if ch == 1:
        add()

    # Call display function
    elif ch == 2:
        display()

    # Call range salary function
    elif ch == 3:
        rangesalary()

    # Exit program
    elif ch == 4:
        print("Program exited")
        break

    # Invalid choice
    else:
        print("Wrong choice")