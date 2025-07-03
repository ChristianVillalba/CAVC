# log in form, will displays:
# error messages if the inputs are not valid or the connection is failing
# success message if the user was correctly logged in 
def login_admin():
    username = username_entry.get().strip()
    password = password_entry.get().strip()
    if not username or not password:
        messagebox.showerror("Error", "Please enter both username and password")
        return
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Admins WHERE username = ? AND password = ?", (username, password))
        result = cursor.fetchone()
        conn.close()
        if result:
            messagebox.showinfo("Success", f"Welcome {username}! You are now logged in.")
            login_frame.destroy()
            root.config(menu=menu_bar)  # Show menu bar after login
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")
    else:
        messagebox.showerror("Error", "Failed to connect to database.")
