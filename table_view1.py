import ttkbootstrap as ttk
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.constants import *

my_w = ttk.Window()
my_w.geometry("1000x6000")  # width and height
colors = my_w.style.colors
l1 = [
    {"text": "id", "stretch": False},
    {"text": "Name", "stretch": True},
    "Class",
    {"text": "Mark"},
    {"text": "Gender"},
]  # Columns with Names and style
# Data rows as list
r_set = [
    (1, "Alex", "Four", 90, "Female"),
    (2, "Ron", "Five", 80, "Male"),
    (3, "Geek", "Four", 70, "Male"),
    (4, "King", "Five", 78, "Female"),
    (5, "Queen", "Four", 60, "Female"),
    (6, "Jack", "Five", 70, "Female"),
]
marks = [r[3] for r in r_set]  # List of all marks column
print(sum(marks))  # sum of the marks column
dv = ttk.tableview.Tableview(
    master=my_w,
    paginated=True,
    coldata=l1,
    rowdata=r_set,
    searchable=True,
    bootstyle=SUCCESS,
    pagesize=10,
    height=10,
    stripecolor=(colors.light, None),
)
dv.grid(row=0, column=0, padx=10, pady=5)
dv.autofit_columns()  # Fit in current view
dv.insert_row("end", values=["-", "---", "All", sum(marks), "All"])
dv.load_table_data()  # Load all data rows
my_w.mainloop()
