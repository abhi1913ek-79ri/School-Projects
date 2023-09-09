""" Progaram for Tkinter Practice"""
from tkinter import *
cal_root=Tk()
cal_root.title("Abhishek programming")

#size
cal_root.geometry('444x545')

#minimize
cal_root.minsize("200","457")

#maximize
cal_root.maxsize("1370","700")



#mainp




    
DAY=Label(cal_root,text="DAY (02)  :",bg="SlateBlue2")
DAY.grid(column=0,row=1)

MONTH=Label(cal_root,text="MONTH(eg.02) :",bg="SlateBlue2")
MONTH.grid(column=0,row=2)
    
YEAR=Label(cal_root,text="YEAR(eg.20  02) :",bg="SlateBlue2")
YEAR.grid(column=0,row=3)

DAYIS=Label(cal_root,text="DAY IS :",bg="SlateBlue2")
DAYIS.grid(column=0,row=4)

K1=StringVar()
    
M1=StringVar()
    
Y1=StringVar() 
    
DAYIS1=StringVar()    
    

    
k=Entry(cal_root,textvariable=K1,fg="midnight blue",bg="navajo white",font="Baskerville 10 bold",borderwidth=4)
k.grid(column=1,row=1)
    
m=Entry(cal_root,textvariable=M1,fg="midnight blue",bg="navajo white",font="Baskerville 10 bold",borderwidth=4)
m.grid(column=1,row=2)
    
y=Entry(cal_root,textvariable=Y1,fg="midnight blue",bg="navajo white",font="Baskerville 10 bold",borderwidth=4)
y.grid(column=1,row=3)

    
dayis=Entry(cal_root,textvariable=DAYIS1,fg="midnight blue",bg="navajo white",font="Baskerville 10 bold",borderwidth=4)
dayis.grid(column=1,row=4)

def findday():
    H=""
    K=K1.get()
    K=int(K)
    M=M1.get()
    M=int(M)
    Y=Y1.get()
    C=int(Y[0:2])
    D=int(Y[2:4])

    
    if M==1:
        M=13
        D=D-1
    if M==2:
        M=14
        D=D-1
    F=(K+(13*(M+1))//5+D+(D//4)+(C//4)-2*C)%7
    if M==13:
        M=1
        D=D+1
    if M==14:
        M=2
        D=D+1

    if K<=31:
            if F==1 :
                    H=("Sunday")
            elif F==2 :
                    H=("Monday")
            elif F==3 :
                    H=("Tuesday")
            elif F==4 :
                    H=("Wednesday")
            elif F==5 :
                    H=("Thursday")
            elif F==6 :
                    H=("Friday")
            elif F==0 :
                    H=("Saturday")
    day_label=Label(dayis,text=H,fg="navajo white",bg="salmon",font="Baskerville 14 bold",borderwidth=4)
    day_label.grid()

    
def ac():
    K1.set("")
    M1.set("")
    Y1.set("")
    DAYIS1.set("")




b1=Button(text="Find",command=findday,bg="aqua",fg="white",padx=6,pady=6,font="Baskerville 14 bold",borderwidth=6)
b1.grid()

b2=Button(text="Reset",command=ac,bg="midnight blue",fg="white",padx=6,pady=6,font="Baskerville 14 bold",borderwidth=6)
b2.grid()

Abhishek_label=Label(cal_root,text="Abhishek 1st GUI APPLICATION",font="Baskerville 10 bold",fg="white",bg="SlateBlue2")
Abhishek_label.grid()

cal_root.config(bg="SlateBlue2")

cal_root.mainloop()
