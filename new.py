from tkinter import *

# Create main window
window = Tk()
window.title("Button Event Example")
window.geometry("300x200")

# Event handler function
def show_message():
    label.config(text="Button Clicked!")

# Label widget
label = Label(window, text="Click the button")
label.pack(pady=10)

# Button widget bound to event handler
button = Button(window, text="Click Me", command=show_message)
button.pack()

# Run application
window.mainloop()