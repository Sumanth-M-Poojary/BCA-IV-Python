"""
2. Program, using user-defined functions to find the area of rectangle, square, circle and triangle by 
accepting suitable input parameters from user.   
"""
def rectangle(l,b):
    return l*b
def square(s):
    return s*s
def circle(r):
    return 3.14*r**2
def triangle(b,h):
    return 0.5*b*h

while True:
    print("\n1. rectangle \n2. Square \n3. Circle \n4. Triangle  \n5.Exit \n-------")
    ch=int(input("your Choice: "))
    if ch==1:
        l=float(input("Length: "))
        b=float(input("Bredth: "))
        area=rectangle(l,b)
        print(f"Area is{area} sq.units")
    elif ch==2:
        s=float(input("Side: "))
        area=square(s)
        print(f"Area is{area}sq.units")
    elif ch==3:
        r=float(input("Radius: "))
        area=circle(r)
        print(f"Area is {area}sq.units")

    elif ch==4:
        b=float(input("Base : "))
        h=float(input("Height : "))
        area=triangle(b,h)
        print(f"Area is {area}sq.units")
    elif ch==5:
        print("\Exiting.....")
        break
    else:
        print("\nwrong Choice!\n")