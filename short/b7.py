from tkinter import *
import pandas as pd
import matplotlib.pyplot as plt


# Add data
def add():

    name = e1.get()
    y2017 = e2.get()
    y2018 = e3.get()
    y2019 = e4.get()
    y2020 = e5.get()

    # Save into CSV file
    f = open("Batsman.csv", "a")

    f.write(name + "," + y2017 + "," + y2018 + "," +
            y2019 + "," + y2020 + "\n")

    f.close()

    print("Saved")


# Show graph
def plot():

    data = pd.read_csv("Batsman.csv")

    data.plot(x="Batsman", kind="bar")

    plt.show()


# Create file with heading
f = open("Batsman.csv", "w")
f.write("Batsman,2017,2018,2019,2020\n")
f.close()


# Window
root = Tk()
root.title("Batsman Scores")
root.geometry("250x250")


# Labels
Label(root, text="Batsman").grid(row=0, column=0)
Label(root, text="2017").grid(row=1, column=0)
Label(root, text="2018").grid(row=2, column=0)
Label(root, text="2019").grid(row=3, column=0)
Label(root, text="2020").grid(row=4, column=0)


# Entry boxes
e1 = Entry(root)
e2 = Entry(root)
e3 = Entry(root)
e4 = Entry(root)
e5 = Entry(root)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)
e5.grid(row=4, column=1)


# Buttons
Button(root, text="Add", command=add).grid(row=5, column=0)

Button(root, text="Plot", command=plot).grid(row=5, column=1)


# Run window
root.mainloop()