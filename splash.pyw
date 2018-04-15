from Tkinter import *
root1=Tk()
root1.title("SPLASH")
import os
def call(event):
    os.startfile("button.py")
    root1.destroy()
Label(root1,text="GUITAR WIDGET",font="times 50 bold").place(x=340,y=50)
Label(root1,text="AVI ANAND",font="times 50 bold").place(x=420,y=150)
Label(root1,text="161B055",font="times 50 bold").place(x=500,y=250)
Label(root1,text="BATCH:BX-B2",font="times 50 bold").place(x=410,y=350)

root1.bind("<Motion>",call)
root1.geometry("1920x1080")
root1.mainloop()

