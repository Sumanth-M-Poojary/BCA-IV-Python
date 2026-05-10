from tkinter import *

def clearall():
    pf.delete(0, END)
    rf.delete(0, END)
    tf.delete(0, END)
    cf.delete(0, END)

def computeCI():
    p = float(pf.get())
    r = float(rf.get())
    t = float(tf.get())

    a = p * (1 + r/100) ** t
    ci = a - p

    cf.delete(0, END)
    cf.insert(0, f"{ci:.2f}")

root = Tk()
root.geometry("280x200")
root.title("Compound Interest")

lb1 = Label(root, text="Principal:")
lb2 = Label(root, text="Rate:")
lb3 = Label(root, text="Time:")
lb4 = Label(root, text="Compound Interest:")

lb1.grid(row=1, column=0, padx=5, pady=5)
lb2.grid(row=2, column=0, padx=5, pady=5)
lb3.grid(row=3, column=0, padx=5, pady=5)
lb4.grid(row=4, column=0, padx=5, pady=5)

pf = Entry(root)
rf = Entry(root)
tf = Entry(root)
cf = Entry(root)

pf.grid(row=1, column=1, padx=5, pady=5)
rf.grid(row=2, column=1, padx=5, pady=5)
tf.grid(row=3, column=1, padx=5, pady=5)
cf.grid(row=4, column=1, padx=5, pady=5)

btn1 = Button(root, text="Submit", command=computeCI)
btn2 = Button(root, text="Clear", command=clearall)

btn1.grid(row=5, column=0, padx=5, pady=5)
btn2.grid(row=5, column=1, padx=5, pady=5)

root.mainloop()