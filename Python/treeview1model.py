import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Treeview widget")
root.geometry("500x500")

#create treeview
treeview = ttk.Treeview(root, columns=("ID","Student","Size", "Modified"),show=("headings"))
treeview.heading("ID", text="Student ID")
treeview.heading("Student", text="Student Name")
treeview.heading("Size", text="File Size")
treeview.heading("Modified", text="Last Modified")


treeview.insert(parent='', index='end', values=("314","Eva","2Tb", "2025-06-12"))
treeview.insert(parent='', index='end', values=("42","Sofia","1Tb", "2025-06-12"))
treeview.insert(parent='', index='end', values=("314","Eva","1Tb", "2025-06-15"))
treeview.insert(parent='', index='end', values=("42","Sofia","4Tb", "2025-06-15"))
treeview.insert(parent='', index='end', values=("42","Sofia","3Tb", "2025-06-15"))

treeview.pack()

root.mainloop()
