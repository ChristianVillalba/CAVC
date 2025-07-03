# validates user inputs before trying to add the information to the database
# will display different errors to guide the users
def register_admin():
        first_name = first_name_entry.get().strip()
        last_name = last_name_entry.get().strip()
        username = username_entry.get().strip()
        password = password_entry.get().strip()
        confirm_password = confirm_password_entry.get()
        email = email_entry.get().strip()
        if not email: # Set to None if blank so it becomes SQL NULL
            email = "NULL"
        #validation
        if not username or not password:
            messagebox.showerror("Error", "Please fill username and password")
            return
        elif len(username) < 8:
            messagebox.showerror("Error", "Username must be at least 8 characters")
            return
        elif len(password) < 8:
            messagebox.showerror("Error", "Password must be at least 8 characters")
            return
        elif password != confirm_password:
            messagebox.showerror("Error", "Passwords don't match")  
            return
        #try to register in the db
        print(f"registred admin: {username}. Welcome to our team, {first_name} {last_name}.")
        messagebox.showinfo( "Success:", f"Success: {username} registred , Welcome to our team, {first_name} {last_name}.")
        result = register_admin_db(first_name, last_name, username, password, email)
        if result is True:
            new_admin_window.destroy()
        elif result is False:
            messagebox.showerror("Error","Username already exists")