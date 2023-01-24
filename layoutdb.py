import tkinter as tk
import sqlite3

root = tk.Tk()
root.geometry("200x200")

colors = ["red", "green", "blue"]

# Connect to the database
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

# Query the data from the database
cursor.execute("SELECT value FROM data")
data = cursor.fetchall()

for i in range(3):
    for j in range(3):
        frame = tk.Frame(root, bg=colors[(i+j) % 3])
        frame.grid(row=i, column=j, sticky="nsew")
        label = tk.Label(frame, text=str(data[i*3+j][0]))
        label.pack()

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.mainloop()

# Close the connection
conn.close()
