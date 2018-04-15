import sqlite3
from Tkinter import *
root=Tk()
con=sqlite3.Connection("db")
cur=con.cursor()
root.geometry('1920x1080')
root.config(background="midnight blue")
root.title("Basic songs")

s=('D','A','G','Bm','Em')
st=str(s)
'''cur.execute("drop table gtr")
cur.execute("create table if not exists gtr(nm varchar(20),keys varchar(20),cha varchar(20),chb varchar(20),dif varchar(20),song varchar(100))")
con.commit()'''
fr = Frame(root, width = 900, height = 85, bg = 'midnight blue')
fr.place(relx= .05, rely = .82)
def add():
    name = e1.get()
    key = e2.get()
    ch1 = e3.get()
    ch2 = e4.get()
    dif = e5.get()
    lyr = t6.get("1.0",END)
    cur.execute("insert into gtr values(?,?,?,?,?,?)",(name,key,ch1,ch2,dif,lyr))
    con.commit()
    
def fetch():
    keyf = e8.get()
    v1 = StringVar()
    v1.set('L')
    name = cur.execute("select nm from gtr where keys = ? or cha = ? or chb = ?",(keyf,keyf,keyf))
    p = .05
    def clear():
        w = fr.place_slaves()
        for i in w:
            i.destroy()
    def show():
        t6.config(state = NORMAL)
        t6.delete('1.0',END)
        val =  v1.get()
        text = cur.execute("select song from gtr where nm = ?",[val]).fetchall()
        t6.insert(END,text[0][0])
        t6.config(state = DISABLED)
        
    for i in name:
        for j in i:
            rd = Radiobutton(fr,text = j.strip('{}'), variable = v1, value = j, command = show, width = 20, anchor = W)
            rd.place(relx = p, rely = .5)
            p = p+0.18
    Button(fr, text = "Clear list", command = clear).place(relx = .5, rely = .75)
  

e1=Entry(root)
e1.place(relx=.25,rely=.1,width=250)
Label(root,text='Name:').place(relx=.1,rely=.1,width=80)
e2=Entry(root)
e2.place(relx=.3,rely=.18)
Label(root,text='Key:').place(relx=.1,rely=.18,width=80)
e3=Entry(root)
e3.place(relx=.3,rely=.26)
Label(root,text='Chord1:').place(relx=.1,rely=.26,width=80)
e4=Entry(root)
e4.place(relx=.3,rely=.34)
Label(root,text='Chord2:').place(relx=.1,rely=.34,width=80)
e5=Entry(root)
e5.place(relx=.3,rely=.42)
Label(root,text='Difficulty:').place(relx=.1,rely=.42,width=80)
t6=Text(root, height = 20, width = 70,bg="gold")
t6.place(relx=.5,rely=.16)
Label(root,text='Lyrics with chords:',font="times 11 bold").place(relx=.5,rely=.1,width=150)
e8=Entry(root)
e8.place(relx=.3,rely=.5)
Label(root,text='Enter chord:').place(relx=.1,rely=.5,width=80)
#e7=Entry(root)
#e7.place(relx=.3,rely=.58)
#Label(root,text='Enter dif:').place(relx=.1,rely=.58)
Button(root,text="Add", command = add).place(relx=.1,rely=.65)
Button(root,text="Find", command = fetch).place(relx=.3,rely=.65)

s = Scrollbar(root)
s.pack(side = RIGHT, fill = Y)
s.config(command = t6.yview)
t6.config(yscrollcommand = s.set)  

root.mainloop()
