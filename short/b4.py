from tkinter import *

# Button click function
def click(value):

    # Clear
    if value == "C":
        e.delete(0, END)

    # Equal
    elif value == "=":

        exp = e.get()
        ans = eval(exp)

        e.delete(0, END)
        e.insert(0, ans)

    # Insert values
    else:
        e.insert(END, value)


# Window
root = Tk()
root.title("Calculator")
root.geometry("250x300")


# Entry box
e = Entry(root, width=25, font=("Arial", 14))
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


# Button list
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+",
    "C"
]


# Create buttons
row = 1
col = 0

for b in buttons:

    Button(root,
           text=b,
           width=5,
           height=2,
           command=lambda x=b: click(x)
           ).grid(row=row, column=col, padx=5, pady=5)

    col += 1

    if col > 3:
        col = 0
        row += 1


# Run window
root.mainloop()