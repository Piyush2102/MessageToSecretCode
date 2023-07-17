from tkinter import *
win=Tk()
#Function for encode\decode
def code():
    x=varr.get()
    st=var.get()
    stt=""
    if(x==0):
        for i in st:
            if(i!=" "):
                stt=stt+chr(ord(i)-26)
            else:
                stt=stt+" "
    if(x==1):
        for i in st:
            if(i!=" "):
                stt=stt+chr(ord(i)+26)
            else:
                stt=stt+" "
    print(stt)
    entr.config(text=stt)
            

#Title and icon
win.title("SPY Code")
win.iconbitmap("icon.ico")

#Window size
win.geometry('800x600')
win.resizable(0,0)

#Background image
bg=PhotoImage(file="bkg.png")
Label(win,image=bg).pack()

#Heading and Input message
Label(win, text ='CODE GENERATOR', font = 'Arial 20 bold',fg="Orange" ,bd=10).place(x=260,y=30)
Label(win, text ='Type message here', font = 'Arial 10 bold', fg="LimeGreen" ,bd=10).place(x=320,y=110)
var=StringVar()
ent=Entry(win,bd=5,textvariable=var,width=60)
ent.place(x=210,y=160,height=120);

#choose message to be encoded or decoded
varr=IntVar()
radio=Radiobutton(win,text="Encode",font='Arial 10 bold',fg="deeppink",value=0,variable=varr).place(x=280,y=290)
radio=Radiobutton(win,text="Decode",font='Arial 10 bold',fg="Purple",value=1,variable=varr).place(x=380,y=290)

#Submit Button
Button(win, font = 'arial 10 bold', text = 'RESULT',fg="brown",padx =2,bg ='LightGray',command=code).place(x=340, y = 330)

#Display
entr=l=Label(win,bd=5,width=60)
entr.place(x=210,y=380,height=120);
win.mainloop()
