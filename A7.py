"""
7. Write a Pandas program to join the two given data frames along rows. Sample Data frame may 
contain details of student like rollno , name , Total Marks.
"""
import pandas as pd

data1={'RollNo':[1,2,3],'Name':['Ria','Avi','Jay'],"TotalMarks":[95,89,90]}
data2={'RollNo':[4,5,6],'Name':['Ana','Lee','Eva'],"TotalMarks":[84,94,97]}


df1=pd.DataFrame(data1)
df2=pd.DataFrame(data2)

print("Given Sample DataFrames:")
print("-"*40)
print(df1)
print("-"*40)
print(df2)
cdf=pd.concat([df1,df2],ignore_index=True)
print("Combined DataFrame:")
print("-"*40)
print(cdf)