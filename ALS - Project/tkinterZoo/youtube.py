import tkinter as tk

# Root component
root = tk.Tk()
root.title("Login Form")
root.geometry("650x600")
root.configure(bg="#C4E1E6")

#frame component
frame = tk.Frame(bg="#C4E1E6")

# Widgets
login_heading = tk.Label(frame, text="Login", bg="#C4E1E6", fg="#213448", font=("Arial", 28))
username_label = tk.Label(frame, text="Username:", bg="#C4E1E6", fg="#213448", font=("Arial", 13))
username_entry = tk.Entry(frame, font=("Arial", 13))
password_label = tk.Label(frame, text="Password:", bg="#C4E1E6", fg="#213448", font=("Arial", 13))
password_entry = tk.Entry(frame, show="*", font=("Arial", 13))
login_button = tk.Button(frame, text="Login", bg="#547792", fg="#ECEFCA", font=("Arial", 13))
# Widgets placement
login_heading.grid(row=0 , column=0, columnspan=2, sticky="news", pady=40) 
username_label.grid(row=1 , column=0, pady=20, padx=10) 
username_entry.grid(row=1 , column=1)
password_label.grid(row=2 , column=0, pady=20, padx=10)
password_entry.grid(row=2 , column=1) 
login_button.grid(row=3 , column=0, columnspan=2, pady=25) 

frame.pack()

root.mainloop()