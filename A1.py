"""
Write a program create list with N elements.  find all unique elements in the list. If an element is 
found only once in the list, then add that element to the unique list.
"""
# Take input for number of elements
n = int(input("Enter total number of elements: "))

# Create an empty list to store all elements
glist = []

# Loop to take input elements from user
for i in range(n):
    glist.append(input(f"Enter element no {i+1}: "))

# Create an empty list to store unique elements
ulist = []

# Loop through each element in the list
for item in glist:
    # Check if the element appears only once in the list
    if glist.count(item) == 1:
        ulist.append(item)

# Print the given list
print("\nGiven list:", glist)

# Check if there are no unique elements
if len(ulist) == 0:
    print("There is no unique element in the list")
else:
    # Print the list of unique elements
    print("List of unique elements are:", ulist)