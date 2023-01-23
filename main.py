import ttkbootstrap as tb
from tkinter import *
from ttkbootstrap.constants import *
root = tb.Window(themename="superhero")
root.title("TTKBootstrap")
# root.iconbitmap("icon.ico")
root.geometry("500x500")

my_label = tb.Label(root, text="Hello World", font=(
    "Helvetica", 18), bootstyle="primary")
my_label.pack(pady=50)
root.mainloop()
