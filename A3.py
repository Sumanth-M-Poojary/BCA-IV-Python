"""
3. Consider a tuple t1= (1,2,5,7,9,2,4,6,8,10). Write a program to perform following operations:   
a) Print half the values of tuple in one line and the other half in the next line.  
b) Print another tuple whose values are even numbers in the given tuple.   
c) Concatenate a tuple t2= (11,13,15) with t1.   
d) Return maximum and minimum value from this tuple.  
"""

t1 = (1,2,5,7,9,2,4,6,8,10)

print("\nTuple t1 =", t1, "\n")

# a) Print half values
mid = len(t1)//2
print("First half:", t1[:mid])
print("Second half:", t1[mid:])

# b) Tuple of even numbers
even_tuple = ()
for i in t1:
    if i % 2 == 0:
        even_tuple += (i,)

print("\nEven numbers in t1:", even_tuple)


# c) Concatenate t2 with t1
t2 = (11,13,15)
t3 = t1 + t2
print("\nConcatenated tuple:", t3)

# d) Maximum and Minimum
largest = max(t3)
smallest = min(t3)

print("\nMaximum:", largest)
print("Minimum:", smallest)