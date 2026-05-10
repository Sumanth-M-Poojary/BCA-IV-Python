""" Program to create a class Employee with empno, name, depname, designation, age and salary and 
perform    the following function.   
i) Accept details of N employees    
ii) Search given employee using empno  
iii) Display employee details in neat format. 
 """
 
# Employee Class
class Employee:

    # Constructor
    def __init__(self):

        self.empno = input("Enter Employee No: ")
        self.name = input("Enter Name: ")
        self.dept = input("Enter Department: ")
        self.designation = input("Enter Designation: ")
        self.age = input("Enter Age: ")
        self.salary = input("Enter Salary: ")

    # Display method
    def display(self):
        print("***************************************************")
        print("Empno\tName\tDepartment\tDesignation\tAge\tSalary")
        print("***************************************************")
        print(f"{self.empno}\t {self.name}\t {self.dept}\t {self.designation}\t {self.age}\t{ self.salary}")


# Empty list
emp_list = []


# Menu
while True:

    print("\n1.Add")
    print("2.Search")
    print("3.Display")
    print("4.Exit")

    ch = input("Enter Choice: ")

    # Add Employee
    if ch == "1":

        n = int(input("How many employees: "))

        for i in range(n):

            e = Employee()

            emp_list.append(e)

    # Search Employee
    elif ch == "2":

        eno = input("Enter Employee No: ")

        found = False

        for e in emp_list:

            if e.empno == eno:

                e.display()

                found = True

        if found == False:
            print("Employee Not Found")

    # Display All
    elif ch == "3":

        print("\nEmployee Details\n")

        for e in emp_list:

            e.display()

    # Exit
    elif ch == "4":

        print("Exiting...")
        break

    # Invalid choice
    else:

        print("Wrong Choice")