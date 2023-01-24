# This code will create a 3x3 grid of frames,
#  each with a different background color: red, green, and blue.
# The background color of each frame is set by using the bg option and passing in a value from the colors list.
# As the colors list has 3 elements and the grid is 3x3, the color will be cycled.
# The sticky option is set to "nsew" in the grid() method, so the frames will expand and fill the grid cells.
# Also the weight of each row and column is set to 1, so each cell will expand and shrink with the size of the window,
# and the frames will expand and shrink as well.
import tkinter as tk

root = tk.Tk()
root.geometry("200x200")

colors = ["red", "green", "blue"]

for i in range(3):
    for j in range(3):
        frame = tk.Frame(root, bg=colors[(i+j) % 3])
        frame.grid(row=i, column=j, sticky="nsew")
        label = tk.Label(frame, text="({}, {})".format(i, j))
        label.pack()

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.mainloop()
