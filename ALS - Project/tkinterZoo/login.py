import tkinter as tk
import tkinter.font
from tkinter import messagebox

# Function to validate the login
def validate_login():
    userid = username_entry.get()
    password = password_entry.get()

    # You can add your own validation logic here
    if userid == "admin" and password == "password":
        messagebox.showinfo("Login Successful", "Welcome, Admin!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Create the main window
root = tk.Tk()
root.title("Login")
root.geometry('550x500')
root.configure(bg="#E7EFC7")

heading = tk.Label(root, text="Zoo - Login")
cf = tkinter.font.Font(family="Times New Roman", size=18, weight="bold")
heading.configure(font=cf)
heading.pack()


#create a frame
frame = tk.Frame(root, bg="lightskyblue", borderwidth=35)
frame.pack(padx=20, pady=20)

# Create and place the username label and entry
username_label = tk.Label(frame, text="Userid:")
username_label.pack()

username_entry = tk.Entry(frame)
username_entry.pack()

# Create and place the password label and entry
password_label = tk.Label(frame, text="Password:")
password_label.pack()

password_entry = tk.Entry(frame, show="*")  # Show asterisks for password
password_entry.pack()

# Create and place the login button
login_button = tk.Button(frame, text="Login", command=validate_login)
login_button.pack()

# Start the Tkinter event loop
root.mainloop()