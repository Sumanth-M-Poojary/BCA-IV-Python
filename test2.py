# n=int(input("Enter the total number of element "))
# glist=[]
# for i in range(n):
#     glist.append(input(f"Enter the value {i+1} "))
# ulist=[]
# for item in glist:
#     if glist.count(item)==1:
#         ulist.append(item)

# print("Given list ",glist)

# if len(ulist)==0:
#     print("No Unique list ")
# else:
#     print(ulist)
##########################################################################

# def rectangle(l,b):
#     return l*b
# def square(s):
#     return s*s
# def circle(r):
#     return 3.14**r
# def triagle(b,h):
#     return 0.5*b*h

# while True:
#     print("1.Rectangle\n2.Square\n3.Circle\n4.Triagle")
#     ch=int(input("Enter your choice "))
    
#     if ch==1:
#         l=float(input("Enter Lenght "))
#         b=float(input("Enter breadth"))
#         area=rectangle(l,b)
#         print(area)
        
########################################################################################     
"""
3. Consider a tuple t1= (1,2,5,7,9,2,4,6,8,10). Write a program to perform following operations:   
a) Print half the values of tuple in one line and the other half in the next line.  
b) Print another tuple whose values are even numbers in the given tuple.   
c) Concatenate a tuple t2= (11,13,15) with t1.   
d) Return maximum and minimum value from this tuple.  
"""

# t1=(1,2,5,7,9,2,4,6,8,10)

# mid=len(t1)//2

# print("First mid",t1[:mid])
# print("Second mid ",t1[mid:])
# even=()
# for i in t1:
#     if i%2==0:
#       even+=(i,)
# print(even)  

# t2=(11,13,15)
# t3=t1+t2
# print(t3)

# large=max(t3)
# small=min(t3)

# print(large)
# print(small)

############################################################################
# def check(sentence):
#     freq={}
#     for ch in sentence:
#         if ch.isalpha():
#             if ch in freq:
#                 freq[ch]+=1
#             else:
#                 freq[ch]=1
#     return freq

# sen=input("Enter sentence ")
# res=check(sen)

# print("sentence is ")
# for key,val in res.items():
#     print(f"{key}={val}")
############################################################################

# def eqaul(str1,str2):
#     count=0
#     for c1,c2 in zip(str1,str2):
#         if c1 != c2:
#             count+=1
#     count+=abs(len(str1)-len(str2))
    
#     if count>1:
#         return False
#     else:
#         return True
    
# str1=input("Enter string ")
# str2=input("Enter String ")

# if eqaul(str1,str1):
#     print("nearly Equal ")
# else:
#     print("Not Equal ")

import pandas as pd
data1={"Rollno":[1,2,3],"Name":["Sujay","Vijay","Anup"],"Marks":[80,90,50]}
data2={"Rollno":[4,5,6],"Name":["Sujay","Vijay","Anup"],"Marks":[80,90,50]}

df1=pd.DataFrame(data1)
df2=pd.DataFrame(data2)
print("Given Sample dataframe ")
print("*"*45)
print(df1)
print("*"*45)
print(df2)
print("*"*45)
cdf=pd.concat([df1,df2],ignore_index=True)
print("Combained DataFrame")
print("*"*45)
print(cdf)
print()