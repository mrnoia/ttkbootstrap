import ttkbootstrap as tb
from tkinter import *
from ttkbootstrap.constants import *
root = tb.Window(themename="superhero")
root.title("TTKBootstrap")
# root.iconbitmap("icon.ico")
root.geometry("500x500")
counter = 0


def changer():
    global counter
    counter += 1

    if counter % 2 == 0:
        my_label.config(text="Hello World")
    else:
        my_label.config(text="Bye World")


my_label = tb.Label(root, text="Hello World", font=(
    "Helvetica", 18), bootstyle="primary")
my_label.pack(pady=50)
mybutton = tb.Button(root, text="Click Me",
                     bootstyle="success,outline", command=changer)
mybutton.pack(pady=10)
root.mainloop()
