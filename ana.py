from Tkinter import *
root=Tk()
root.title("Understanding Parts Of Guitar")
root.config(background='midnight blue')
#tyr = PhotoImage(file = 'bg.gif')
#Label(root,image=tyr,bd=0).place(x=0,y=0)
root.geometry('1920x1080')
img=PhotoImage(file="label.gif")
p=450

#s = Scrollbar(root)
t = Text(root,height = 20, width = 60, bg = 'gold', font = 'times 15 bold')
#s.pack(side = RIGHT, fill = Y)
t.place(relx = .3, rely = .2)
#s.config(command = t.yview)
#t.config(yscrollcommand = s.set)

t.insert(END,'Select any part of the guitar to know about its functionality !')
t.config(state = DISABLED)

neck="The neck can be a single piece of wood or several pieces glued together and cut to shape.\
The fretboard is a separate piece of wood that is attached to the neck. Necks can be glued\
to the body (set neck) or bolted on. Set necks are usually found on acoustic guitars and many\
other instruments including the violin, lute and cello. The bolt-on neck is a design feature\
more commonly associated with electric guitars. Most necks are wood though alternative materials\
such as carbon fibre composites have been used."

fret="The fretboard is a piece of wood that is glued to the front of the neck. These are commonly made\
of rosewood though other hard woods such as ebony may also be used. Embedded in the fretboard are a number\
of metal frets (fret-wire) usually numbering twenty to twenty-four. Strings are pressed down behind a fret\
which changes the length that is left free to vibrate thereby producing a different note. A simple\
demonstration is to be found on the twelfth fret. On all guitars this is the fret that divides the string\
exactly in half and produces a note an octave higher than the open note. Any open string that maintains its\
original tension and is halved produces its octave. This applies to all stringed instruments including the piano and violin."

key="Tuning pegs are used to raise and lower the pitch of the strings. Acoustic guitars have two rows\
of three pegs which, when the guitar is held as normal, presents one row at the top of the headstock and\
one row at the bottom. Electric guitars may have tuning pegs in a single row running along the top of\
the headstock (Fender Stratocaster) or use the the acoustic guitar arrangement (Gibson Les Paul).\
The tuning pegs act as string terminators and it is essential for tuning stability that they suffer no defects.\
Tuning pegs that are misaligned, have play or excessive resistance to turning may need repair or replacing.\
Tuning pegs can be mounted to a plate, three on a single plate for acoustics, or attached to the headstock as individual pegs"

head="The headstock lies at the end of the guitar's neck. The purpose of the headstock is to support the tuners, which\
terminates the strings of the instrument. The tuners are attached to tuning pegs and this allows the guitarist to lower\
or raise the pitch of the string. A secondary purpose of the headstock is identification and many guitar manufacturers\
choose to use a distinctive headstock shape often in combination with the name of the model and a trademark logo. On some\
guitars the model name and trademark logo may be created using inlaid materials though decals are also commonly used."

fretboard="The fretboard is a piece of wood that is glued to the front of the neck. These are commonly made of rosewood though\
other hard woods such as ebony may also be used. Embedded in the fretboard are a number of metal frets (fret-wire) usually numbering\
twenty to twenty-four. Strings are pressed down behind a fret which changes the length that is left free to vibrate thereby\
producing a different note. A simple demonstration is to be found on the twelfth fret. On all guitars this is the fret\
that divides the string exactly in half and produces a note an octave higher than the open note. Any open string that maintains\
its original tension and is halved produces its octave. This applies to all stringed instruments including the piano and violin."

strings="A string is the vibrating element that produces sound in string instruments such as the guitar, harp,\
piano (piano wire), and members of the violin family. Strings are lengths of a flexible material that a musical\
instrument holds under tension so that they can vibrate freely, but controllably. Strings may be 'plain'\
(consisting only of a single material, like steel, nylon, or gut). 'Wound' strings have a 'core' of one material,\
with an overwinding of other materials. This is to make the string vibrate at the desired pitch, while maintaining\
a low profile and sufficient flexibility for playability."

machine="A machine head (also referred to as a tuning machine, tuner, or gear head) is a geared apparatus for tuning\
stringed musical instruments by adjusting string tension. Machine heads are used on mandolins, guitars, double basses etc.,\
and are usually located on the instrument's headstock. Non-geared tuning devices that are used on violins, violas, cellos,\
lutes, older Flamenco guitars, ukuleles etc., are known as friction pegs. Friction pegs hold the string in tune by way of friction\
caused by their tapered shape and by the string pull created by the tight string. Some other commonly used slang names for guitar\
tuners are pegs, gears, machines, cranks, knobs, tensioners and tighteners."

strap="If you have a guitar strap, available from any guitar store for a few dollars, then you can also learn to play standing.\
This is useful if you plan on playing in a band. If you have a heavy guitar a broad guitar strap is often more comfortable than a\
thin strap. To attach a strap, there should be a hole in each end that you can put over two pins, usually fitted on the endblock\
of the guitar and where the neck meets the body. Many acoustic guitars only have one pin on the end block, and straps must be attached\
under the strings above the nut on the headstock. However, this sometimes makes it difficult for keep the guitar at an optimum\
height and can cause shoulder strain. You can usually install a second pin where the neck meets the body, but you should be\
careful or you might damage (and devalue) your guitar."

marker="The white dots are typically placed at harmonic points on the string. The first harmonic of the open string is the octave,\
halfway along the string at the 12th fret. The second harmonic is one-third the string length, and that falls at the seventh fret. On\
some models, you'll see that fret marked with a double-dot as well, as it's a very prominent harmonic:\
The woman holding the guitar here is pointing at the octave marker, but you can see the seventh fret is also double-dotted"

binding="Binding, for both bodies and necks, is primarily to provide sacrificial material for minor dings and dents, which\
is why it's placed on edges and occasionally on the sides of fretboards.Fretboard binding has the added bonus of preventing\
or at least hiding the edges of frets from sticking out and making fretting uncomfortable. Sometimes frets are poorly installed\
or more likely the fretboard wood shrinks slightly as it dries out which can make the frets stick out. The biggest problem with\
fretboard binding is that it can make refretting the guitar more difficult and more expensive."

rosette="Originally, the rosette, which would simply have been a couple of concentric rings of hardwood inlayed around the\
soundhole, was to strengthen this area from cracking, either from dryness or an accidental hit.\
Ofcourse the rosette evolved to become a blend of function (reinforcement) and artistic beauty. Still, internal reinforcement\
on the inside of the top, under the rosette is a good idea, as this area is still prone to the occasional crack."

top="Some electric guitars have an extra top added to the body to blend the tonal qualities of different types of wood together.\
Maple with figuring is a popular top and produces a pronounced look and tone (adds brightness). Body tops are not used\
on acoustics since the layering of two pieces of wood for the table would inhibit the resonance and dull the tone."

pickgaurd="Guitars, in common with all wood instruments, are prone to dents, scratches and wear. A pick guard\
(also known as a scratch plate) protects the body of the guitar at the point of most contact. Some electric guitars have\
raised pick guards so your pick is directed out and away from the pots and strings. Pick guards sometimes need replacing due\
to wear or damage. In the case of an expensive or rare guitar, which may have a tortoise shell pick guard, the guitar will\
have to be sent to an experienced luthier."

bridge="The bridge is found on the lower bout of the body and its function is to allow the strings to sit at a relative \
height to the fretboard. Depending on the guitar, the strings may terminate at the bridge or just pass over it. On electric\
guitars the bridge can be raised or lowered using two screws (thumbscrews which can be rotated with the fingers or traditional\
screws requiring a screwdriver) at either end of the bridge. This is discussed further in the Adjusting the Guitar section."

a=(neck,fret,key,head,fretboard,strings,machine,strap,marker,binding,rosette,top,pickgaurd,bridge)

def sel(x):
    if x=="neck":
        t.config(state = NORMAL)
        t.delete(1.0,END)
        t.insert(END, neck)
        Label(root,text='Neck', font = 'times 20 bold',bg='OrangeRed3').place(relx = .3, rely = .1,width=400)
        t.config(state = DISABLED)
    elif x=="fret":
        t.config(state = NORMAL)
        t.delete(1.0,END)
        t.insert(END, fret)
        Label(root,text='Fret', font = 'times 20 bold',bg='OrangeRed3').place(relx = .3, rely = .1,width=400)
        t.config(state = DISABLED)
    elif x=="key":
        t.config(state = NORMAL)
        t.delete(1.0,END)
        t.insert(END, key)
        Label(root,text='Key', font = 'times 20 bold',bg='OrangeRed3').place(relx = .3, rely = .1,width=400)
        t.config(state = DISABLED)
    elif x=="head":
        t.config(state = NORMAL)
        t.delete(1.0,END)
        t.insert(END, head)
        Label(root,text='Head', font = 'times 20 bold',bg='OrangeRed3').place(relx = .3, rely = .1,width=400)
        t.config(state = DISABLED)
    elif x=="fretboard":
        t.config(state = NORMAL)
        t.delete(1.0,END)
        t.insert(END, fretboard)
        Label(root,text='Fretboard', font = 'times 20 bold',bg='OrangeRed3').place(relx = .3, rely = .1,width=400)
        t.config(state = DISABLED)
    elif x=="strings":
        t.config(state = NORMAL)
        t.delete(1.0,END)
        t.insert(END, strings)
        Label(root,text='Strings', font = 'times 20 bold',bg='OrangeRed3').place(relx = .3, rely = .1,width=400)
        t.config(state = DISABLED)
    elif x=="machine":
        t.config(state = NORMAL)
        t.delete(1.0,END)
        t.insert(END, machine)
        Label(root,text='Machine head', font = 'times 20 bold',bg='OrangeRed3').place(relx = .3, rely = .1,width=400)
        t.config(state = DISABLED)
    elif x=="strap":
        t.config(state = NORMAL)
        t.delete(1.0,END)
        t.insert(END, strap)
        Label(root,text='Strap button', font = 'times 20 bold',bg='OrangeRed3').place(relx = .3, rely = .1,width=400)
        t.config(state = DISABLED)
    elif x=="marker":
        t.config(state = NORMAL)
        t.delete(1.0,END)
        t.insert(END, marker)          
        Label(root,text='Position marker', font = 'times 20 bold',bg='OrangeRed3').place(relx = .3, rely = .1,width=400)
        t.config(state = DISABLED)
    elif x=="binding":
        t.config(state = NORMAL)
        t.delete(1.0,END)
        t.insert(END, binding)
        Label(root,text='Binding', font = 'times 20 bold',bg='OrangeRed3').place(relx = .3, rely = .1,width=400)
        t.config(state = DISABLED)
    elif x=="rosette":
        t.config(state = NORMAL)
        t.delete(1.0,END)
        t.insert(END, rosette)
        Label(root,text='Rosette', font = 'times 20 bold',bg='OrangeRed3').place(relx = .3, rely = .1,width=400)
        t.config(state = DISABLED)
    elif x=="top":
        t.config(state = NORMAL)
        t.delete(1.0,END)
        t.insert(END, top)
        Label(root,text='Top', font = 'times 20 bold',bg='OrangeRed3').place(relx = .3, rely = .1,width=400)
        t.config(state = DISABLED)
    elif x=="pickgaurd":
        t.config(state = NORMAL)
        t.delete(1.0,END)
        t.insert(END, pickgaurd)
        Label(root,text='Pickgaurd', font = 'times 20 bold',bg='OrangeRed3').place(relx = .3, rely = .1,width=400)
        t.config(state = DISABLED)
    elif x=="bridge":
        t.config(state = NORMAL)
        t.delete(1.0,END)
        t.insert(END, bridge)
        Label(root,text='Bridge', font = 'times 20 bold',bg='OrangeRed3').place(relx = .3, rely = .1,width=400)
        t.config(state = DISABLED)
    
#--------------------------------------------------------------------------------------------------------------------------------------
Label(root,image=img).place(y=5,x=500-p)
Button(root,text="neck",command=lambda:sel("neck")).place(x=570-p,y=215)
Button(root,text="frets",command=lambda:sel("fret")).place(x=565-p,y=165)
Button(root,text="key",command=lambda:sel("key")).place(x=540-p,y=100)
Button(root,text="head",command=lambda:sel("head")).place(x=515-p,y=30)
Button(root,text="fretboard",command=lambda:sel("fretboard")).place(x=690-p,y=200)
Button(root,text="strings",command=lambda:sel("strings")).place(x=690-p,y=120)
Button(root,text="machine head",command=lambda:sel("machine")).place(x=680-p,y=35)
Button(root,text="strap button",command=lambda:sel("strap")).place(x=530-p,y=300)
Button(root,text="position marker",command=lambda:sel("marker")).place(x=675-p,y=305)
Button(root,text="binding",command=lambda:sel("binding")).place(x=710-p,y=350)
Button(root,text="rosette",command=lambda:sel("rosette")).place(x=510-p,y=390)
Button(root,text="top",command=lambda:sel("top")).place(x=510-p,y=480)
Button(root,text="pickgaurd",command=lambda:sel("pickgaurd")).place(x=710-p,y=460)
Button(root,text="bridge",command=lambda:sel("bridge")).place(x=510-p,y=680)

'''frame = Frame(root,height = 400, width = 450)
frame.place(y= 50,x=400)'''

root.mainloop()
