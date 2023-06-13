import ttkbootstrap as ttk
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.constants import *
import sqlite3

my_w = ttk.Window()
my_w.geometry("400x300")  # width and height
colors = my_w.style.colors
l1 = [
    {"text": "id", "stretch": False},
    {"text":"Name","stretch":True},
    "Last name",
    {"text":"email"},
    {"text":"car make"},
    {"text":"car model"},
    {"text":"car year"},
    {"text":"car price"},
]  # Columns with Names and style 
# Data rows as list 
conn = sqlite3.connect('epood_dmahdi.db')
c = conn.cursor()
c.execute('SELECT * FROM tabel')
results = c.fetchall()
r_set = results

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
dv.autofit_columns() # Fit in current view 
dv.insert_row("end", values=['-', "---", "All", "All"])
dv.load_table_data() # Load all data rows 
my_w.mainloop()