#6. Write a program to create a text file and compute the number of characters, words and lines in a file
# Ask user to enter file name
fname = input("Enter file name: ")

# Open file in write mode and take input from user
with open(fname, "w") as f:
    print("Enter the contents into file :")
    
    while True:
        try:
            f.write(input())   # Write user input to file
            f.write("\n")      # Add new line after each input
        except EOFError:
            break              # Stop when user presses EOF (Ctrl+D / Ctrl+Z)

# Initialize counters
cc = 0   # character count
wc = 0   # word count
lc = 0   # line count

# Open file in read mode to count contents
with open(fname, "r") as f:
    for line in f:
        lc += 1                      # Count number of lines
        wc += len(line.split())      # Count words in each line
        cc += len(line.strip("\n"))  # Count characters (excluding newline)

# Display results
print(f"\nLines = {lc} \nWords = {wc} \nCharacters = {cc}")