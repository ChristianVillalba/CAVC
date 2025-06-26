import tkinter as tk
import pyodbc
from tkinter import messagebox

#main window (root component)
root = tk.Tk()
root.title("Zoo App")
root.geometry("750x650")
root.configure(bg="#C4E1E6")

# Database Connection:
# Database credentials
SERVER = 'laptop-n0755o44\\sqlexpress01'  # Or 'localhost\\SQLEXPRESS' if using a named instance
DATABASE = 'zooDB'
USERNAME = 'LAPTOP-N0755O44\\CRISTIAN'
DRIVER = 'ODBC Driver 18 for SQL Server'
#Connect & test functions:
def get_db_connection():
    """Establish a connection to SQL Server using ODBC."""
    try:
        conn = pyodbc.connect(
            f'DRIVER={{ODBC Driver 17 for SQL Server}};'
            f'SERVER={SERVER};'
            f'DATABASE={DATABASE};'
            f'UID={USERNAME};'
            f'Encrypt=yes;'
            f'TrustServerCertificate=yes;'
            "Trusted_Connection=yes;"
        )
        return conn
    except Exception as e:
        print(f"Database connection failed: {e}")
        return None
def test_connection():
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            sqlquery = "SELECT * FROM admins"
            cursor.execute(sqlquery)
            results = cursor.fetchall()
            if results:
                for row in results:
                    print(row)  # Prints each row as a tuple
            else:
                print("No records found in Tasks table.")
        except Exception as e:
            print(f"Error during query execution: {e}")
        finally:
            conn.close()
    else:
        print("Failed to establish a connection.")
# call the test function
test_connection()

# Application functionality:
# login (mandotory to use the app):
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
# manage admis: CRUD OPERATIONS to Admins Table (sql db)
def manage_admins_window():
    crud_admins_window = tk.Toplevel()
    crud_admins_window.title("Manage Admins")
    crud_admins_window.geometry("750x650")
    crud_admins_window.configure(bg="#C4E1E6")
    crud_admins_window.resizable(True, True)
    crud_admins_window.grab_set() # functionality. user can't interact with other windows.
    def load_admins():
        admin_listbox.delete(0, tk.END) # clear the content of an entry widget
        conn = get_db_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Admins")
            rows = cursor.fetchall()
            conn.close()
            for row in rows:
                admin_listbox.insert(tk.END, f"{row[0]} - {row[2]}, {row[1]}")
    def delete_admin():
        selection = admin_listbox.get(tk.ACTIVE)
        if not selection:
            messagebox.showwarning("Warning", "Please select an admin to delete.")
            return
        admin_id = selection.split(" - ")[0]
        confirm = messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete Admin {admin_id}?")
        if not confirm:
            messagebox.showinfo("Cancelled", "Deletion cancelled.")
            return
        conn = get_db_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Admins WHERE admin_id = ?", (admin_id,))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Admin deleted successfully.")
            load_admins()
    def edit_admin():
        selection = admin_listbox.get(tk.ACTIVE)
        if not selection:
            messagebox.showwarning("Warning", "Please select an admin to edit.")
            return
        admin_id = selection.split(" - ")[0]
        edit_window = tk.Toplevel()
        edit_window.title("Edit Admin")
        edit_window.geometry("400x450")
        edit_window.configure(bg="#C4E1E6")
        edit_window.grab_set()
        conn = get_db_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT first_name, last_name, username, email FROM Admins WHERE admin_id = ?", (admin_id,))
            row = cursor.fetchone()
            conn.close()
        tk.Label(edit_window, text="Edit Admin", font=("Arial", 20, "bold"), bg="#C4E1E6", fg="#213448").pack(pady=20)
        tk.Label(edit_window, text="First Name:", font=("Arial", 12), bg="#C4E1E6", anchor="w").pack(pady=(10, 0))
        entry_first = tk.Entry(edit_window, font=("Arial", 12))
        entry_first.pack(pady=5)
        entry_first.insert(0, row[0])
        tk.Label(edit_window, text="Last Name:", font=("Arial", 12), bg="#C4E1E6", anchor="w").pack(pady=(10, 0))
        entry_last = tk.Entry(edit_window, font=("Arial", 12))
        entry_last.pack(pady=5)
        entry_last.insert(0, row[1])
        tk.Label(edit_window, text="Username:", font=("Arial", 12), bg="#C4E1E6", anchor="w").pack(pady=(10, 0))
        entry_user = tk.Entry(edit_window, font=("Arial", 12))
        entry_user.pack(pady=5)
        entry_user.insert(0, row[2])
        tk.Label(edit_window, text="Email:", font=("Arial", 12), bg="#C4E1E6", anchor="w").pack(pady=(10, 0))
        entry_email = tk.Entry(edit_window, font=("Arial", 12))
        entry_email.pack(pady=5)
        entry_email.insert(0, row[3])
        def save_changes():
            new_first = entry_first.get().strip()
            new_last = entry_last.get().strip()
            new_user = entry_user.get().strip()
            new_email = entry_email.get().strip()
            conn = get_db_connection()
            if conn:
                cursor = conn.cursor()
                cursor.execute("""
                    UPDATE Admins
                    SET first_name = ?, last_name = ?, username = ?, email = ?
                    WHERE admin_id = ?
                """, (new_first, new_last, new_user, new_email, admin_id))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Admin updated successfully.")
                edit_window.destroy()
                load_admins()
        tk.Button(edit_window, text="Save Changes", font=("Arial", 12), bg="#16610E", fg="white", width=15, command=save_changes).pack(pady=30)
    # Title Label
    tk.Label(crud_admins_window, text="Manage Admins", font=("Arial", 22, "bold"), bg="#C4E1E6", fg="#213448").pack(pady=20)
    # Listbox
    admin_listbox = tk.Listbox(crud_admins_window, width=50, height=15, font=("Arial", 12))
    admin_listbox.pack(pady=10)
    # Buttons
    button_frame = tk.Frame(crud_admins_window, bg="#C4E1E6")
    button_frame.pack(pady=20)
    tk.Button(button_frame, text="Reload", font=("Arial", 12), bg="#41729F", fg="white", width=12, command=load_admins, cursor="exchange").grid(row=0, column=0, padx=10)
    tk.Button(button_frame, text="Edit", font=("Arial", 12), bg="#FFB200", fg="black", width=12, command=edit_admin,cursor="pencil").grid(row=0, column=1, padx=10)
    tk.Button(button_frame, text="Delete", font=("Arial", 12), bg="#D72638", fg="white", width=12, command=delete_admin, cursor="pirate").grid(row=0, column=2, padx=10)
    load_admins()
# register a new admin:
def register_admin_db(first_name, last_name, username, password, email):
    print(f'Attempting to register user: {username}')
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT username FROM Admins WHERE username = ?",(username,))
        user = cursor.fetchone()
        if user:
            print(f"User {username} already exists")
            conn.close
            return False
        cursor.execute("INSERT INTO Admins(first_name, last_name, username, password, email) VALUES(?,?,?,?,?)",(first_name, last_name, username, password, email))
        conn.commit()
        print(f"user {username} registered successfully")
        conn.close
        return True
def create_admin_user_window():
    new_admin_window = tk.Toplevel() #creates extra screen, secondary pop up window
    new_admin_window.title("Register New Admin")
    new_admin_window.geometry("750x650")
    new_admin_window.configure(bg="#C4E1E6")
    new_admin_window.resizable(True, True)
    #functionality
    new_admin_window.grab_set() #The user can’t interact with any other window in your app until this one is closed or released.
    #adds to database new user
    def register_admin():
        first_name = first_name_entry.get().strip()
        last_name = last_name_entry.get().strip()
        username = username_entry.get().strip()
        password = password_entry.get().strip()
        confirm_password = confirm_password_entry.get()
        email = email_entry.get().strip()
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
    #create a frame
    frame = tk.Frame(new_admin_window, bg="#C4E1E6", borderwidth=35)
    frame.pack(padx=20, pady=10)
    # Widgets
    register_heading = tk.Label(frame, text="Create New Admin", bg="#C4E1E6", fg="#213448", font=("Arial", 28, "bold"))
    first_name_label = tk.Label(frame, text="First name:", bg="#C4E1E6", fg="#213448", font=("Arial", 13))
    first_name_entry = tk.Entry(frame, font=("Arial", 13))
    last_name_label = tk.Label(frame, text="Last name:", bg="#C4E1E6", fg="#213448", font=("Arial", 13))
    last_name_entry = tk.Entry(frame, font=("Arial", 13))
    email_label = tk.Label(frame, text="Email:", bg="#C4E1E6", fg="#213448", font=("Arial", 13))
    email_entry = tk.Entry(frame, font=("Arial", 13))
    username_label = tk.Label(frame, text="Username:", bg="#C4E1E6", fg="#213448", font=("Arial", 13))
    username_entry = tk.Entry(frame, font=("Arial", 13))
    password_label = tk.Label(frame, text="Password:", bg="#C4E1E6", fg="#213448", font=("Arial", 13))
    password_entry = tk.Entry(frame, show="*", font=("Arial", 13))
    confirm_password_label = tk.Label(frame, text="Confirm password:", bg="#C4E1E6", fg="#213448", font=("Arial", 13))
    confirm_password_entry = tk.Entry(frame, show="*", font=("Arial", 13))
    cancel_button = tk.Button(frame, command=new_admin_window.destroy,text="Cancel", bg="#DC2525", fg="#ECEFCA", cursor="pirate", font=("Arial", 13))
    register_button = tk.Button(frame, command=register_admin ,text="Register", bg="#16610E", fg="#ECEFCA",cursor="heart", font=("Arial", 13))
    # Widgets placement
    register_heading.grid(row=0 , column=0, columnspan=2, sticky="news", pady=40) 
    first_name_label.grid(row=1 , column=0, pady=10, padx=10) 
    first_name_entry.grid(row=1 , column=1)
    last_name_label.grid(row=2 , column=0, pady=10, padx=10) 
    last_name_entry.grid(row=2 , column=1)
    email_label.grid(row=3 , column=0, pady=10, padx=10) 
    email_entry.grid(row=3 , column=1)
    username_label.grid(row=4 , column=0, pady=10, padx=10) 
    username_entry.grid(row=4 , column=1)
    password_label.grid(row=5 , column=0, pady=10, padx=10)
    password_entry.grid(row=5 , column=1) 
    confirm_password_label.grid(row=6 , column=0, pady=10, padx=10)
    confirm_password_entry.grid(row=6 , column=1) 
    cancel_button.grid(row=7 , column=0, pady=25)
    register_button.grid(row=7 , column=1,  pady=25) 
    #call frame
    frame.pack()

# welcome / login window
welcome_heading = tk.Label(root, text="Welcome to ZooApp", bg="#C4E1E6", fg="#213448", font=("Arial", 28, "bold"))
welcome_heading.pack(pady=10)
# Login frame & login form
login_frame = tk.Frame(root, bg="#C4E1E6", borderwidth=35)
login_frame.pack(padx=20, pady=50)
admin_heading = tk.Label(login_frame, text="Please, login to use the application", bg="#C4E1E6", fg="#213448", font=("Arial", 16, "bold"))
admin_heading.grid(row=0, column=0, columnspan=2, pady=10)
username_label = tk.Label(login_frame, text="Username:", bg="#C4E1E6", fg="#213448", font=("Arial", 13))
username_label.grid(row=1, column=0, pady=10, padx=10)
username_entry = tk.Entry(login_frame, font=("Arial", 13))
username_entry.grid(row=1, column=1)
password_label = tk.Label(login_frame, text="Password:", bg="#C4E1E6", fg="#213448", font=("Arial", 13))
password_label.grid(row=2, column=0, pady=10, padx=10)
password_entry = tk.Entry(login_frame, show="*", font=("Arial", 13))
password_entry.grid(row=2, column=1)
login_button = tk.Button(login_frame, text="Login", bg="#16610E", fg="#ECEFCA", cursor="hand2", font=("Arial", 13), command=login_admin)
login_button.grid(row=3, column=0, columnspan=2, pady=20)

#navigation menu
menu_bar = tk.Menu(root)
#create login menu
admin_menu = tk.Menu(menu_bar, tearoff=1)
menu_bar.add_cascade(label="Admin Managment", menu=admin_menu)
admin_menu.add_command(label="Manage Admins", command=manage_admins_window)
admin_menu.add_command(label="Create New Admin",command=create_admin_user_window)


root.config(menu=menu_bar)
# call application
root.mainloop()