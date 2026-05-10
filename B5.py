import mysql.connector

# Connect to MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="studentdb2"
)

cur = conn.cursor()

# Function to insert student details
def add_student():
    regno = int(input("Enter RegNo: "))
    name = input("Enter Name: ")
    m1 = int(input("Enter Mark1: "))
    m2 = int(input("Enter Mark2: "))
    m3 = int(input("Enter Mark3: "))

    query = "INSERT INTO student  VALUES (%s, %s, %s, %s, %s)"
    values = (regno, name, m1, m2, m3)

    try:
        cur.execute(query,values)
        conn.commit()
        print("Student record inserted successfully.")
    except mysql.connector.IntegrityError:
        print("student already in db")

# Function to display all students
def display_students():
    query = "SELECT * FROM student"
    cur.execute(query)

    rows = cur.fetchall()

    print("\nStudent Details")
    print("RegNo\tName\tM1\tM2\tM3")

    for row in rows:
        print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}")

    print()

# Function to delete student by regno
def delete_student():
    regno = int(input("Enter RegNo to delete: "))

    query = "DELETE FROM student WHERE regno = %s"
    value = (regno,)

    cur.execute(query, value)
    conn.commit()

    if cur.rowcount > 0:
        print("Student record deleted successfully.\n")
    else:
        print("Record not found.\n")

# Main Menu
while True:
    print("1. Add Student")
    print("2. Display Students")
    print("3. Delete Student")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_student()

    elif choice == 2:
        display_students()

    elif choice == 3:
        delete_student()

    elif choice == 4:
        break

    else:
        print("Invalid Choice")

# Close connection
cur.close()
conn.close()