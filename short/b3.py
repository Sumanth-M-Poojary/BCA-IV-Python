
"""
3.Create a GUI to input Principal amount, rate of interest and number of years, Calculate Compound 
interest. When button submit is pressed Compound interest should be displayed in a textbox. When 
clear button is pressed all contents should be cleared. 
"""

from tkinter import *

# Calculate Compound Interest
def calculate():

    p = float(e1.get())
    r = float(e2.get())
    t = float(e3.get())

    ci = p * (1 + r/100) ** t - p

    e4.delete(0, END)
    e4.insert(0, ci)


# Clear all boxes
def clear():

    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)


# Window
root = Tk()
root.title("Compound Interest")
root.geometry("300x200")


# Labels
Label(root, text="Principal").grid(row=0, column=0)
Label(root, text="Rate").grid(row=1, column=0)
Label(root, text="Time").grid(row=2, column=0)
Label(root, text="Compound Interst").grid(row=3, column=0)


# Entry boxes
e1 = Entry(root)
e2 = Entry(root)
e3 = Entry(root)
e4 = Entry(root)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)


# Buttons
Button(root, text="Calculate", command=calculate).grid(row=4, column=0)

Button(root, text="Clear", command=clear).grid(row=4, column=1)


# Run window
root.mainloop()