import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

root.title("Tkinter - Message Box")
root.geometry('550x500+100-70')

#Function to confirm action (messagebox)
def confirm_action():
    response = messagebox.askyesno("Confirmation", "Do you want to proceed?")
    if response: 
        messagebox.showinfo("Proceeding", "You choose to proceed.")
    else: messagebox.showinfo("Cancelled", "You chose to cancel.")


# label1 = tk.Label(root, text="Hello World!")
# label1.pack() 
button = tk.Button(root, text="Confirmation Action", command=confirm_action)
button.pack(pady=20)
root.mainloop()
root.mainloop()