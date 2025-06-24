import tkinter as tk
import pyodbc
from tkinter import *
from tkinter import messagebox
#main window (root component)
root = tk.Tk()
root.title("ToDoApp")
root.geometry("650x600")
# root.configure(bg="#C4E1E6")

# background image try-except estatement example:
try:
    bg_img = PhotoImage(file="bg.png")
    bg_label = Label(root, image=bg_img)  # Use the actual image object here
    bg_label.place(relwidth=1, relheight=1)
except:
    print("Image failed to load:")
    root.config(bg="#C4E1E6")

# Database Connection
SERVER = 'laptop-n0755o44\\sqlexpress01'  # Or 'localhost\\SQLEXPRESS' if using a named instance
DATABASE = 'SimpleToDoApp'
USERNAME = 'LAPTOP-N0755O44\\CRISTIAN'
DRIVER = 'ODBC Driver 18 for SQL Server'
 
def get_db_connection():
    """Establish a connection to SQL Server using ODBC."""
    try:
        conn = pyodbc.connect(
            f'DRIVER={{ODBC Driver 18 for SQL Server}};'
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
            sqlquery = "SELECT * FROM Users"
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

test_connection()

#functionality

# to insert a new user in the db
def register_user_db(username, password):
    print(f'Attempting to register user: {username}')
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT username FROM Users WHERE username = ?",(username,))
        user = cursor.fetchone()
        if user:
            print(f"User {username} already exists")
            conn.close
            return False
        cursor.execute("INSERT INTO Users(username,password) VALUES(?,?)",(username, password))
        conn.commit()
        print(f"user {username} registered successfully")
        conn.close
        return True
# except Exception as e:
#     print(f"Error registering user: {e}")
#     conn.close()
def create_new_user_window():
    login_window = tk.Toplevel() #creates extra screen, secondary pop up window
    login_window.title("Create New User")
    login_window.geometry("650x600")
    login_window.configure(bg="#C4E1E6")
    login_window.resizable(False, True)
    #functionality
    login_window.grab_set() #The user can’t interact with any other window in your app until this one is closed or released.
    #adds to database new user
    def register_user():
        username = username_entry.get().strip()
        password = password_entry.get()
        confirm_password = confirm_password_entry.get()
        #validation
        if not username or not password:
            messagebox.showerror("Error, please fill both boxes")
            return
        elif len(username) < 8:
            messagebox.showerror("Error, username must be at least 8 characters")
            return
        elif len(password) < 8:
            messagebox.showerror("Error, password must be at least 8 characters")
            return
        elif password != confirm_password:
            messagebox.showerror("Error, passwords don't match")  
            return
        #try to register in the db
        print(f"register user: {username}")
        result = register_user_db(username,password)
        if result is True:
            login_window.destroy()
        elif result is False:
            messagebox.showerror("Username already exists")
        elif result is False:
            messagebox.showerror("Username already exists")


    #create a frame
    frame = tk.Frame(login_window, bg="#C4E1E6", borderwidth=35)
    frame.pack(padx=20, pady=20)
    # Widgets
    register_heading = tk.Label(frame, text="Register", bg="#C4E1E6", fg="#213448", font=("Arial", 28, "bold"))
    username_label = tk.Label(frame, text="Username:", bg="#C4E1E6", fg="#213448", font=("Arial", 13))
    username_entry = tk.Entry(frame, font=("Arial", 13))
    password_label = tk.Label(frame, text="Password:", bg="#C4E1E6", fg="#213448", font=("Arial", 13))
    password_entry = tk.Entry(frame, show="*", font=("Arial", 13))
    confirm_password_label = tk.Label(frame, text="Confirm password:", bg="#C4E1E6", fg="#213448", font=("Arial", 13))
    confirm_password_entry = tk.Entry(frame, show="*", font=("Arial", 13))
    cancel_button = tk.Button(frame, command=login_window.destroy,text="Cancel", bg="#DC2525", fg="#ECEFCA", cursor="pirate", font=("Arial", 13))
    register_button = tk.Button(frame, command=register_user ,text="Register", bg="#16610E", fg="#ECEFCA",cursor="heart", font=("Arial", 13))
    
    # Widgets placement
    register_heading.grid(row=0 , column=0, columnspan=2, sticky="news", pady=40) 
    username_label.grid(row=1 , column=0, pady=20, padx=10) 
    username_entry.grid(row=1 , column=1)
    password_label.grid(row=2 , column=0, pady=20, padx=10)
    password_entry.grid(row=2 , column=1) 
    confirm_password_label.grid(row=3 , column=0, pady=20, padx=10)
    confirm_password_entry.grid(row=3 , column=1) 
    cancel_button.grid(row=4 , column=0, pady=25)
    register_button.grid(row=4 , column=1,  pady=25) 

    #call frame
    frame.pack()
    # I hope I don't need to use this:
    #button_frame = Frame=(login_window)
    #button_frame.pack(pady=15)
    #Button(button_frame, text="register", bg="green", width=16).pack(side=RIGHT, padx=5)
    #Button(button_frame, text="cancel", bg="red", width=16).pack(side=Left, padx=5)





# welcome heading
login_heading = tk.Label(root, text="Welcome", bg="#C4E1E6", fg="#213448", font=("Arial", 28, "bold"))
login_heading.pack(pady=20)

navigation_instructions = tk.Label(root, text="Please, use the manu bar to navigate", bg="#C4E1E6", fg="#213448", font=("Arial", 16))
navigation_instructions.pack(pady=20)

#navigation menu
menu_bar = tk.Menu(root)

#create login menu
login_menu = tk.Menu(menu_bar, tearoff=1)
menu_bar.add_cascade(label="Login", menu=login_menu)
login_menu.add_command(label="Create account", command=create_new_user_window)

root.config(menu=menu_bar)
# call application
root.mainloop()



