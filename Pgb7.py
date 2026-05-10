from tkinter import *
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import messagebox
import os

def Add():
    bats = baf.get()
    scores = [f2017.get(), f2018.get(), f2019.get(), f2020.get()]

    if bats == "" or "" in scores:
        messagebox.showwarning("Input Error", "Please fill all fields")
        return

    with open("Batsman.csv", "a") as f:
        f.write(f"{bats},{','.join(scores)}\n")

    messagebox.showinfo("Batsman", "Details saved")

    # Clear fields
    baf.delete(0, END)
    f2017.delete(0, END)
    f2018.delete(0, END)
    f2019.delete(0, END)
    f2020.delete(0, END)


def showplot():
    try:
        data = pd.read_csv("Batsman.csv")
        data.plot(x="Batsman", kind="bar", title="Score Card")
        plt.xlabel("Batsman")
        plt.ylabel("Runs")
        plt.show()
    except:
        messagebox.showerror("Error", "No data to display")


# Create file only if not exists
if not os.path.exists("Batsman.csv"):
    with open("Batsman.csv", "w") as f:
        f.write("Batsman,2017,2018,2019,2020\n")

root = Tk()
root.title("Scores")
root.geometry("250x300")

# Labels
Label(root, text="Batsman").grid(row=0, column=0, padx=5, pady=5)
Label(root, text="2017").grid(row=1, column=0)
Label(root, text="2018").grid(row=2, column=0)
Label(root, text="2019").grid(row=3, column=0)
Label(root, text="2020").grid(row=4, column=0)

# Entry fields
baf = Entry(root)
f2017 = Entry(root)
f2018 = Entry(root)
f2019 = Entry(root)
f2020 = Entry(root)

baf.grid(row=0, column=1)
f2017.grid(row=1, column=1)
f2018.grid(row=2, column=1)
f2019.grid(row=3, column=1)
f2020.grid(row=4, column=1)

# Buttons
Button(root, text="Add", command=Add).grid(row=5, column=0, pady=10)
Button(root, text="Plot", command=showplot).grid(row=5, column=1)

root.mainloop()