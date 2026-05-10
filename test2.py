n=int(input("Enter the total number of element "))
glist=[]
for i in range(n):
    glist.append(input(f"Enter the value {i+1} "))
ulist=[]
for item in glist:
    if glist.count(item)==1:
        ulist.append(item)

print("Given list ",glist)

if len(ulist)==0:
    print("No Unique list ")
else:
    print(ulist)