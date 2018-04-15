from Tkinter import *
import os
root=Tk()
root.title("Guitar widget")
root.geometry('1920x1080')
def songs():
    os.startfile("database.pyw")
def diag():
    os.startfile("guitar_trans.pyw")
def parts():
    os.startfile("ana.pyw")
root.config(bg = 'gold')


img1=PhotoImage(file="chor.gif")
Button(root,image=img1,command=songs).place(x=650,y=50)
Label(root,text="Songs",font= "times 25 bold", bg = 'gold').place(x=710,y=260)
img2=PhotoImage(file="hand.gif")
Button(root,image=img2,command=diag).place(x=350,y=50)
Label(root,text="Learn Chords",font= "times 25 bold", bg = 'gold').place(x=350,y=260)
img3=PhotoImage(file="parts.gif")
Button(root,image=img3,command=parts).place(x=50,y=50)
Label(root,text="Anatomy",font= "times 25 bold", bg = 'gold').place(x=90,y=260)
#root.minsize(500,500)

root.minsize(500,500)
root.mainloop()
