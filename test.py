# import mysql.connector

# conn=mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="studentdb2"
# )
# cur=conn.cursor()
# def add():
#     regno=int(input("Enter register number "))
#     name=input("Enter student  name ")
#     m1=int(input("Mark 1: "))
#     m2=int(input("Mark 2: "))
#     m3=int(input("Mark 3: "))
#     query="INSERT INTO student VALUES(%s,%s,%s,%s,%s )"
#     values=(regno,name,m1,m2,m3)
    
#     try:
#         cur.execute(query,values)
#         conn.commit()
#         print("Student record inserted successfully.")
#     except mysql.connector.IntegrityError:
#         print("student already in db")
       
# def display():
#     qry="select *from student"
#     cur.execute(qry,)
#     rows=cur.fetchall()
#     print("Student Details ")
#     print("Regno\tname\tm1\tm2\tm3\t")
#     for row in rows:
#         print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}")
#     print()

# def delete():
#     regno=int(input("Enter regno to delete "))
#     qry="delete from student where regno =%s"
#     value=(regno,)
#     cur.execute(qry,value)
#     conn.commit()
#     if cur.rowcount>0:
#         print("deleted successfull ")
#     else:
#         print("no record found ")
# while True:
#     print("1.add student\n2.display \n3.Delete \n4.exit")
#     ch=int(input("Enter your choice "))
#     if ch==1:
#         add()
#     elif ch==2:
#         display()
#     elif ch==3:
#         delete()
#     else:
#         print("wrong ")

##################################################################

# import mysql.connector
# conn=mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="studentdb2"
#  )

# cur=conn.cursor()

# def add():
#     eno=int(input("Enter employee number "))
#     name=input("Enter name ")
#     salary=int(input("salary "))
#     qry="insert into employee values(%s,%s,%s)"
#     values=(eno,name,salary)
    
#     try:
#         cur.execute(qry,values)
#         conn.commit()
#         print("Details Saved ")
#     except mysql.connector.IntegrityError:
#         print("Employee already In database ")
        
# def display():
#     eno=int(input("Enter empno "))
#     qry="select *  from employee where eno=%s"
#     value=(eno, )
#     cur.execute(qry,value)
#     rows=cur.fetchone()
#     print("Empolyee details ")
#     print("Empno\t ename  \t salary ")
#     if cur.rowcount>0:
#         print(f"{rows[0]}\t{rows[1]}\t{rows[2]}")

# def rangesalary():
#     min=int(input("Enter minimum salary "))
#     max=int(input("Enter maximum salary "))
#     qry="select * from employee where salary between %s and %s"
#     value=(min,max)
#     cur.execute(qry,value)
#     rows=cur.fetchall()
#     for row in rows:
#         print("Emp details ")
#         print("Emp. No \t Emp. Name \tSalary")
#         print(f"{row[0]}\t{row[1]}\t{row[2]}")
# while True:
#     print("1.add Employee\n2.Get Employee \n3.show Employee \n4.Exit")
#     ch=int(input("Enter choice "))
#     if ch==1:
#         add()
#     elif ch==2:
#         display()
#     elif ch==3:
#         rangesalary()  
#     elif ch==4:
#         break
#     else:
#         print("wrong choice ")    
        
#################################################################
#B1

# class employee:
#     def __init__(self):
#         self.empno=input("Enter employee number ")
#         self.name=input("Enter employee name ")
#         self.depname=input("Enter department ")
#         self.designation=input("Enter Designation ")
#         self.age=int(input("Enter Age "))
#         self.salary=input("Enter salary ")

#     def display(self):
#         print(f"{self.empno}{self.name}{self.depname}{self.designation}{self.age}{self.salary}")
        
# emp_list=[]

# while True:
#     print("ADD\nSearch\nDisplay\nExit")
#     ch=int(input("Enter your choice  "))

#     if ch==1:
#         n=int(input("Enter Number of employee  "))
#         for i in range(n):
#             e=employee()
#             emp_list.append(e)
#     elif ch==2:
#         eno=input("Enter employee number ")
#         found=False
#         for e in emp_list:
#             if e.empno==eno:
#                 e.display()
#                 found=True
#         if found==False:
#             print("Employee not found  ")
#     elif ch==3:
#         for e in emp_list:
#             e.display()

# class BankAccount:
#     def __init__(self):
#         self.balance=0
    
#     def deposit(self,amount):
#         self.balance=self.balance+amount
#         print("Deposit successfully ",amount)
    
#     def withdraw(self,amount):
#        if amount>self.balance:
#            print("Insufficient Balance ")
#        else:
#            self.balance=self.balance-amount
#            print("Withdraw Amount ",amount)
#     def show(self):
#         print("Balance ",self.balance)
        
# class SavingAccount(BankAccount):
#     def __init__(self):
#         super().__init__()
#         self.rate=0
    
#     def set(self,rate):
#         self.rate=rate;
        
#     def add_interest(self):
#         interst=(self.balance*self.rate)/100
#         self.balance=self.balance+interst
#         print("Interst added ",interst)
# acc=SavingAccount()

# while True:
#     print("\n1.Deposit")
#     print("2.Withdraw")
#     print("3.Show Balance")
#     print("4.Set Interest Rate")
#     print("5.Add Interest")
#     print("6.Exit")
    
#     ch=int(input("Enter your choice "))
    
#     if ch==1:
#         amount=float(input("Enter amount "))
#         acc.deposit(amount)
#     elif ch==2:
#         amount=float(input("Enter amount " ))
#         acc.withdraw(amount)
#     elif ch==3:
#         acc.show()
#     elif ch==4:
#         r=float(input("Enter Interst rate "))
#         acc.set(r)
#     elif  ch==5:
#         acc.add_interest()
# from tkinter import *

# def calculate():
#     p=float(e1.get())
#     r=float(e2.get())
#     t=float(e3.get())
#     ci=p*(1+r/100)**t-p
    
#     e4.delete(0,END)
#     e4.insert(0,ci)
    
# def clear():
#     e1.delete(0,END)
#     e2.delete(0,END)
#     e3.delete(0,END)
#     e4.delete(0,END)
    
# root=Tk()
# root.title("Compute Interest")
# root.geometry("300x200")

# Label(root,text="Principal").grid(row=0,column=0)
# Label(root,text="Rate").grid(row=1,column=0)
# Label(root,text="Time").grid(row=2,column=0)
# Label(root,text="Compound Interest").grid(row=3,column=0)

# e1=Entry(root)
# e2=Entry(root)
# e3=Entry(root)
# e4=Entry(root)

# e1.grid(row=0,column=1)
# e2.grid(row=1,column=1)
# e3.grid(row=2,column=1)
# e4.grid(row=3,column=1)

# Button(root,text="Compute", command=calculate).grid(row=4,column=0)
# Button(root,text="clear", command=clear).grid(row=4,column=1)
# root.mainloop()

from tkinter import *

def  click(value):
    if value=="C":
        e.delete(0,END)
    elif value=="=":
        exp=e.get()
        ans=eval(exp)
        e.delete(0,END)
        e.insert(0,ans)
        
    else:
        e.insert(END,value)
        
root=Tk()
root.title("Calculator")
root.geometry("250x300")

e=Entry(root,width=20,font=("Arial",14))
e.grid(row=0,column=0,columnspan=4)

buttons=[
    "7","8","9","+",
    "4","5","6","*",
    "1","2","3","/",
    "0",".","=","-",
    "C"
]

row=1
col=0

for b in buttons:
    Button(root,text=b,height=2,width=5,command=lambda x=b:click(x)).grid(row=row,column=col,padx=10,pady=10)
    col+=1
    if col>3:
        col=0
        row+=1

root.mainloop()