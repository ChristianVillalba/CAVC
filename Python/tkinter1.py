from tkinter import * # Import Module
import tkinter.font #to change font in lable1 element

root = Tk() # create root window

root.title("Hello tkinter")
root.geometry('550x500+100-70') # Set geometry (widthxheight)
# root.resizable(True, False) (widthxheight)

label1 = Label(root, text="Hello World!")
label1.pack() # if you don't add a pack function, Label won't be displayed
# Change Font display in lable1
cf = tkinter.font.Font(family="Times New Roman", size=18, weight="bold")
label1.configure(font=cf)

label2 = Label(root, text="Second Label!")
label2.pack() 

def clicked(): #callback function, will change label2
    label2.configure(text = "I just got clicked")
# button widget with red color text inside
btn = Button(root, text = "Click me" , 
             fg="red",
             command=clicked)
btn.pack()

# Entry widget
label3 = Label(root, text="Enter your name!")
label3.pack()
entry = Entry(root)
entry.pack()

# Radio buttons widget
radioVar = IntVar()
def radioSelection():
   selection = "You selected the option " + str(radioVar.get())
   label.config(text = selection)
option1 = Radiobutton(root, text="Option 1", variable=radioVar, value=1, command=radioSelection)
option1.pack()
option2 = Radiobutton(root, text="Option 2", variable=radioVar, value=2, command=radioSelection)
option2.pack()
label = Label(root)
label.pack()

button1 = Button(root, text="Disabled Button 1", state=DISABLED, background="gold")
button1.pack()

button2 = Button(root, text="Working Button 2")
button2.pack()

listboxlabel = Label(root, text = "Food Items") 
listboxlabel.pack()
# Define the size and styles of the listbox element
listbox = Listbox(root, 
                  height = 6, # x = number of elements that could take space
                  width = 10, 
                  bg = "silver",
                  activestyle = 'dotbox', 
                  font = "Helvetica",
                  fg = "maroon")

# insert elements by their
# index and names.
listbox.insert(1, "Nachos")
listbox.insert(2, "Sandwich")
listbox.insert(3, "Burger")
listbox.insert(4, "Pizza")
listbox.insert(5, "Burrito")
# pack the widgets
listbox.pack()

messingMyLabel = Label(root, text = "poiuytrewqlkjhgfdsamnbvcxz", width=100, wraplength=50) 
messingMyLabel.pack()

textWidget = Text(root, height = 5, width = 52)


# runs tkinter. runs all the script above 
root.mainloop()
