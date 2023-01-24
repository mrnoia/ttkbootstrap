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

labels = []

for i in range(3):
    for j in range(3):
        frame = tk.Frame(root, bg=colors[(i+j) % 3])
        frame.grid(row=i, column=j, sticky="nsew")
        label = tk.Label(frame, text=str(data[i*3+j][0]))
        label.place(relx=0.5, rely=0.5, anchor='center')
        labels.append(label)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)


def on_resize(event):
    # print(event.widget)
    if event.widget == root:
        width = event.width
        height = event.height
        font_size = int(max(width, height) // 15)
        print(font_size)
        for label in labels:
            label.configure(font=("Helvetica", font_size))


root.bind("<Configure>", on_resize)
root.mainloop()

# Close the connection
conn.close()
