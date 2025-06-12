from tkinter import *
from tkinter import messagebox

root = Tk()

root.title("Hospital App")
root.geometry('550x500+100-70')

def check_fever():
    return("hello")
def check_cough():
    return("hello")
def check_headache():
    return("hello")
def scedule_appointment():
    return("hello")

btn_check_fever = Button(root, text = "Check Fever" , command=check_fever)
btn_check_fever.pack()
btn_check_cough = Button(root, text = "Click Cough" , command=check_cough)
btn_check_cough.pack()
btn_check_headache = Button(root, text = "Click Headache" , command=check_headache)
btn_check_headache.pack()
btn_scedule_appointment = Button(root, text = "Click Scedule Appointment" , command=scedule_appointment)
btn_scedule_appointment.pack()

root.mainloop()