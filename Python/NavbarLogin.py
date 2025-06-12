import tkinter as Tk
from tkinter import messagebox
from tkinter import *
#create the main window
 
#creating function
 
def new_file():
    messagebox.showinfo("About", "This is a simple menu bar example.")
 
def exit_app():
    root.quit()
 
#function for login
def new_user():
# creating a window
   login_window =Toplevel(root)
   login_window.title ("New user registration")
   login_window.geometry("300x200")
   login_window.resizable(False, True)
   
   #center in window
   login_window.transient(root)
   login_window.grab_set()
   
   # CREATING LABELS AND ENTRY FIELDS
   Label(login_window , text ="new user", font=(" Arial", 14 )).pack(pady =5)
   Label(login_window , text ="username").pack(pady =5)
   username_entry = Entry(login_window, width =25)
   username_entry.pack(pady =5)
   
   Label(login_window , text ="password").pack(pady =5)
   password_entry = Entry(login_window, width =25, show ="*")
   password_entry .pack(pady =5)
                                     
   Label(login_window , text ="confirm password").pack(pady =5)
   confirm_password_entry = Entry(login_window, width =25, show ="*")
   confirm_password_entry .pack(pady =5)
   #nested function of new user
   
   def register_user():
       username = username_entry.get()
       password = password_entry.get()
       confirm_password =confirm_password_entry.get()
       
    # conditions
       if not username or not password:
           messagebox.showerror("please fill in all fields")
       elif password != confirm_password:  
            messagebox.showerror("passowrd do not match")
       else:
            messagebox.showinfo("sucess", f"welcome back,{username}!")
            login_window.destroy()
           
    #button
btn1=Frame(login_window)
btn1.pack(pady=15)

Button(btn1, text="Register", command=register_user, bg="green").pack(side=LEFT,padx=5 )

Button(btn1, text="cancel", command=login_window.destroy, bg="green").pack(side=LEFT ,padx=5)  
 
 
#def existing_user():
#    login_window =Toplevel(root)
#  login_window.title ("USER LOGIN")
#   login_window.geometry("300x200")
#   login_window.resizable(False, True)
   
  # LABELS
 
   
root =Tk()
root.title("Menu Bar")
root.geometry("300x200")
 
#create a menu bar
menu_bar = Menu(root)
 
#creating a file menu
 
file_menu = Menu(menu_bar,tearoff=0 )
file_menu.add_command(label= "New", command=new_file)
file_menu.add_separator()
file_menu.add_command(label= "Exit", command=exit_app)
menu_bar.add_cascade(label="File", menu=file_menu)
 
#create a help menu
help_menu = Menu(menu_bar,tearoff=0 )
help_menu.add_command(label= "roundabout", command=lambda:messagebox.askyesno("do you want to get full information "))
menu_bar.add_cascade(label="Help me!!", menu=help_menu)
 
# creating a login window
login_menu = Menu(menu_bar,tearoff=0 )
login_menu.add_command(label= "New user", command=new_user)
login_menu.add_command(label= "Existing user", command=existing_user)
menu_bar.add_cascade(label="login", menu=login_menu)
 
 
root.config(menu =menu_bar)
 
root.mainloop()