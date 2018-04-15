from Tkinter import *
root=Tk()
#root1=Tk()
root.configure(background='midnight blue')
root.title("Guitar Chords Training")
w = Canvas(root, width=400, height=500,bg="gold",highlightthickness=0)
x=0
y=0
w.pack()
root.geometry('1920x1080')
def clear():
    li = w.place_slaves()
    for l in li:
        l.destroy()

for i in range(0,5):
           w.create_line(98,100+x,302,100+x,width=4)
           i=i+1
           x=x+76
for i in range(0,6):
           w.create_line(100+y,100,100+y,402,width=4)
           y=y+40
def call(a,b,c,d,e,f,g='1'):
          
           #a.destroy()
           clear()
           l1=Label(w,text='o',bg="black",fg="white").place(x=98-10,y=98-48+(76*a),height=20,width=20)
           l2=Label(w,text='o',bg="black",fg="white").place(x=98-10+(40*1),y=98-48+(76*b),height=20,width=20)
           l3=Label(w,text='o',bg="black",fg="white").place(x=98-10+(40*2),y=98-48+(76*c),height=20,width=20)
           l4=Label(w,text='o',bg="black",fg="white").place(x=98-10+(40*3),y=98-48+(76*d),height=20,width=20)
           l5=Label(w,text='o',bg="black",fg="white").place(x=98-10+(40*4),y=98-48+(76*e),height=20,width=20)
           l6=Label(w,text='o',bg="black",fg="white").place(x=98-10+(40*5),y=98-48+(76*f),height=20,width=20)
           l7=Label(w,text=g,bg="black",fg="white").place(x=50,y=125,height=20,width=20)
           Label(w,text="Fret:",bg="gold",fg="black",font="times 8").place(x=10,y=125,height=20,width=20)
           Label(w,text="Open Notes:",bg="gold",fg="black",font="times 10 bold").place(x=8,y=50)

def get():
#Major---------------------------
    if v1.get()==1:
        if v2.get()==1:
            call(0,0,2,2,2,0)
        elif v2.get()==2:
            call(1,1,3,3,3,1)
        elif v2.get()==3:
            call(2,2,4,4,4,2)
        elif v2.get()==4:
            call(0,3,2,0,1,0)
        elif v2.get()==5:
            call(1,4,3,1,2,1)
        elif v2.get()==6:
            call(0,0,0,2,3,2)
        elif v2.get()==7:
            call(1,4,3,1,2,1,3)
        elif v2.get()==8:
            call(0,2,2,1,0,0)
        elif v2.get()==9:
            call(1,3,3,2,1,1)
        elif v2.get()==10:
            call(2,4,4,3,2,2)
        elif v2.get()==11:
            call(3,2,0,0,0,3)
        elif v2.get()==12:
            call(2,4,4,3,2,2,3)
#minor---------------------------
    elif v1.get()==2:
        if v2.get()==1:
            call(0,0,2,2,1,0)
        elif v2.get()==2:
            call(1,1,3,3,2,1)
        elif v2.get()==3:
            call(2,2,4,4,3,2)
        elif v2.get()==4:
            call(1,1,3,3,2,1,3)
        elif v2.get()==5:
            call(2,2,4,4,3,2,3)
        elif v2.get()==6:
            call(0,0,0,2,3,1)
        elif v2.get()==7:
            call(0,0,1,3,4,2)
        elif v2.get()==8:
            call(0,2,2,0,0,0)
        elif v2.get()==9:
            call(1,3,3,1,1,1)
        elif v2.get()==10:
            call(2,4,4,2,2,2)
        elif v2.get()==11:
            call(1,3,3,1,1,1,3)
        elif v2.get()==12:
            call(2,4,4,2,2,2,3)
#seventh---------------------------
    elif v1.get()==3:
        if v2.get()==1:
            call(0,0,2,0,2,0)
        elif v2.get()==2:
            call(1,1,3,1,3,1)
        elif v2.get()==3:
            call(0,2,1,2,0,2)
        elif v2.get()==4:
            call(0,3,2,3,1,0)
        elif v2.get()==5:
            call(0,4,3,4,2,0)
        elif v2.get()==6:
            call(0,0,0,2,1,2)
        elif v2.get()==7:
            call(0,0,1,3,2,3)
        elif v2.get()==8:
            call(0,2,0,1,0,0)
        elif v2.get()==9:
            call(1,3,1,2,1,1)
        elif v2.get()==10:
            call(2,4,2,3,2,2)
        elif v2.get()==11:
            call(1,3,1,2,1,1,3)
        elif v2.get()==12:
            call(2,4,2,3,2,2,3)
#MAJ 7th---------------------------
    elif v1.get()==4:
        if v2.get()==1:
            call(0,0,2,1,2,0)
        elif v2.get()==2:
            call(1,1,3,2,3,1)
        elif v2.get()==3:
            call(2,2,4,3,4,2)
        elif v2.get()==4:
            call(0,3,2,0,0,0)
        elif v2.get()==5:
            call(1,4,3,1,1,1)
        elif v2.get()==6:
            call(0,0,0,2,2,2)
        elif v2.get()==7:
            call(0,0,1,3,3,3)
        elif v2.get()==8:
            call(0,2,1,1,0,0)
        elif v2.get()==9:
            call(0,0,3,2,1,0)
        elif v2.get()==10:
            call(0,0,4,3,2,1)
        elif v2.get()==11:
            call(0,0,4,3,2,1,2)
        elif v2.get()==12:
            call(0,0,4,3,2,1,3)
          
   
v1=IntVar()
v2=IntVar()
Button(root, text = 'clear', command = clear,width=20).pack()
#Button(root,text='submit',command=lambda:call(1,1,1,1,1,1)).pack()
Button(root,text='submit',command=get,width=20).pack()
#Button(root,text='MAJOR2',command=lambda:call(1,1,1,1,1,1)).pack()
Label(root,text="CATEGORY",font="times 20 bold",bg="orange").place(x=30,y=5)
Radiobutton(root,text='Major',indicatoron=0,width=5,padx=20,variable=v1,value=1).place(x=10,y=50)
Radiobutton(root,text='minor',indicatoron=0,width=5,padx=20,variable=v1,value=2).place(x=10,y=85)
Radiobutton(root,text='seventh',indicatoron=0,width=5,padx=20,variable=v1,value=3).place(x=10,y=120)
Radiobutton(root,text='maj7',indicatoron=0,width=5,padx=20,variable=v1,value=4).place(x=10,y=155)
Radiobutton(root,text='A  ',width=5,variable=v2,value=1).place(x=145,y=50)
Radiobutton(root,text='A#',width=5,variable=v2,value=2).place(x=145,y=80)
Radiobutton(root,text='B  ',width=5,variable=v2,value=3).place(x=145,y=110)
Radiobutton(root,text='C  ',width=5,variable=v2,value=4).place(x=145,y=140)
Radiobutton(root,text='C#',width=5,variable=v2,value=5).place(x=145,y=170)
Radiobutton(root,text='D  ',width=5,variable=v2,value=6).place(x=145,y=200)
Radiobutton(root,text='D#',width=5,variable=v2,value=7).place(x=145,y=230)
Radiobutton(root,text='E  ',width=5,variable=v2,value=8).place(x=145,y=260)
Radiobutton(root,text='F  ',width=5,variable=v2,value=9).place(x=145,y=290)
Radiobutton(root,text='F#',width=5,variable=v2,value=10).place(x=145,y=320)
Radiobutton(root,text='G  ',width=5,variable=v2,value=11).place(x=145,y=350)
Radiobutton(root,text='G#',width=5,variable=v2,value=12).place(x=145,y=380)

#Button(root,text='MAJOR',command=lambda:des).pack()
root.minsize(600,600)
mainloop()
#call(0,0,0,0,0,0)
