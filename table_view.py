import ttkbootstrap as ttk
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.constants import *

app = ttk.Window()
colors = app.style.colors

coldata = [
    {"text": "LicenseNumber", "stretch": False},
    "CompanyName",
    {"text": "UserCount", "stretch": False},
]

rowdata = [
    ("A123", "IzzyCo", 12),
    ("A136", "Kimdee Inc.", 45),
    ("A158", "Farmadding Co.", 36),
]

dt = Tableview(
    master=app,
    coldata=coldata,
    rowdata=rowdata,
    paginated=True,
    searchable=True,
    bootstyle=PRIMARY,
    stripecolor=(colors.light, None),
)
dt.pack(fill=BOTH, expand=YES, padx=10, pady=10)
# make the table expand to fit the window when it is expanded
app.rowconfigure(0, weight=1)
app.columnconfigure(0, weight=1)


dt.autofit_columns()
app.mainloop()
