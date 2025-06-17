import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Treeview 2nd Example")
root.geometry("500x500")

treeview = ttk.Treeview(root)
treeview["columns"] = ("Name", "Age", "City")

# Define columns using a py list
treeview.column("#0", width=-0, stretch=tk.NO) #hides default column
treeview.column("Name",anchor=tk.W, width=120)
treeview.column("Age",anchor=tk.CENTER, width=50)
treeview.column("City",anchor=tk.W, width=120)
# Create Headings
treeview.heading("#0", text="", anchor=tk.W)
treeview.heading("Name", text="Name", anchor=tk.W)
treeview.heading("Age", text="Age", anchor=tk.CENTER)
treeview.heading("City", text="City", anchor=tk.W)
# Insert Data
treeview.insert("", "end", values=("Alicia","30","Canada"))
treeview.insert("", "end", values=("Katie","17","UK"))
treeview.insert("", "end", values=("Megan","18","France"))

treeview.pack(pady=20, fill="both", expand=True)

root.mainloop()