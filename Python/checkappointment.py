from tkinter import *
import tkinter.font
from tkinter import messagebox

root = Tk()

root.title("Hospital App")
root.geometry('650x600+100-70')

heading = Label(root, text="Hospial App")
cf = tkinter.font.Font(family="Times New Roman", size=18, weight="bold")
heading.configure(font=cf)
heading.pack()

#create a frame
frame = Frame(root, bg="lightskyblue", borderwidth=35)
frame.pack(padx=20, pady=20)


def check_fever():
    return("hello")
def check_cough():
    return("hello")
def check_headache():
    return("hello")
def schedule_appointment():
    response = messagebox.askyesno("Confirmation", "Do you want to book an appointment?")
    if response: 
        messagebox.showinfo("Proceeding", "Appointment Booked for 15/6/25 at 11:00")
    else: messagebox.showinfo("Cancelled", "You chose to cancel.")



#instead of root, connect to frame
btn_check_fever = Button(frame, text = "Check Fever" , command=check_fever)
btn_check_fever.pack()
btn_check_cough = Button(frame, text = "Click Cough" , command=check_cough)
btn_check_cough.pack()
btn_check_headache = Button(frame, text = "Click Headache" , command=check_headache)
btn_check_headache.pack()
btn_schedule_appointment = Button(frame, text = "Click Schedule Appointment" , command=schedule_appointment)
btn_schedule_appointment.pack()

root.mainloop()