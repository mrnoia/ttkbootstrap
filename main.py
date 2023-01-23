# This code creates a simple graphical user interface(GUI) using the ttkbootstrap library, which is a wrapper for the tkinter library.
# The GUI consists of a single window with a label and a button.
# The window is created using the ttkbootstrap.Window class and is given the theme "superhero." T
# he title of the window is set to "TTKBootstrap" and the window's size is set to 500x500 pixels.
# A global variable "counter" is initialized to 0.
# The function "changer" increments the counter variable by 1 and check if the counter modulus 2 is equal to 0.
# If so, the text of the label is set to "Hello World" and if not , the text of the label is set to "Bye World"
# A label is created using the ttkbootstrap.
# Label class and is given the initial text "Hello World" and font "Helvetica" of size 18 and bootstyle "primary".
# The label is then displayed on the window using the pack() method.
# A button is created using the ttkbootstrap.
# Button class and is given the text "Click Me", bootstyle "success,outline" and command "changer" which calls the function changer when the button is clicked .
# The button is then displayed on the window using the pack() method.
# Finally, the tkinter event loop is started using the mainloop() method to make the window visible and responsive to user input.


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
