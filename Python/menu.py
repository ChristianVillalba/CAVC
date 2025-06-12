from tkinter import *
from tkinter import messagebox

def exit_app():
    return("h1")
def confirm_action():
    response = messagebox.askyesno("Confirmation", "Do you like strawberries?")
    if response: 
        messagebox.showinfo("Proceeding", "I also like strawberries.")
    else: messagebox.showinfo("Cancelled", "Great! More straberries for me!.")

    
root = Tk()
root.title("Tkinter - Navbar")
root.geometry('550x500+100-70')

menu_bar = Menu(root)
#Creating File Menu
file_menu = Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="File Menu", menu=file_menu)
file_menu.add_command(label ='New File', command = None)
file_menu.add_command(label ='Open...', command = None)
file_menu.add_command(label ='Save', command = None)
file_menu.add_separator()
file_menu.add_command(label ='Exit App', command = root.destroy)
#Creating Help Menu
file_menu = Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="Help Menu", menu=help)
#Approval Message
approve_menu = Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="Approve", command=confirm_action)

root.config(menu=menu_bar)

root.mainloop()