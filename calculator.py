from tkinter import*

def laxClick(numbers):
    global oper
    oper=oper+str(numbers)
    t_Input.set(oper)

def laxClearDis():
    global oper
    oper=""
    t_Input.set("")

def laxEqualsInput():
    global oper
    sumup=str(eval(oper))
    t_Input.set(sumup)
    oper=""

a=Tk()
a.title(" A  *ORPAT CALCULATOR*  L" )
oper=""
t_Input=StringVar()

txtDis=Entry(a,font=("Arial",20,"bold"),textvar=t_Input, bd=25,insertwidth=4,bg="light green", justify="right").grid(columnspan=4)

lax=Button(a,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="7",bg="sky blue",command=lambda:laxClick(7)).grid(row=1,column=0)

lax=Button(a,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="8",bg="sky blue",command=lambda:laxClick(8)).grid(row=1,column=1)

lax=Button(a,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="9",bg="sky blue",command=lambda:laxClick(9)).grid(row=1,column=2)

Mult=Button(a,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="*",bg="sky blue",command=lambda:laxClick("*")).grid(row=1,column=3)

lax=Button(a,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="4",bg="sky blue",command=lambda:laxClick(4)).grid(row=2,column=0)

lax=Button(a,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="5",bg="sky blue",command=lambda:laxClick(5)).grid(row=2,column=1)

lax=Button(a,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="6",bg="sky blue",command=lambda:laxClick(6)).grid(row=2,column=2)

sub=Button(a,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="-",bg="sky blue",command=lambda:laxClick("-")).grid(row=2,column=3)

lax=Button(a,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="3",bg="sky blue",command=lambda:laxClick(3)).grid(row=3,column=0)

lax=Button(a,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="2",bg="sky blue",command=lambda:laxClick(2)).grid(row=3,column=1)

lax=Button(a,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="1",bg="sky blue",command=lambda:laxClick(1)).grid(row=3,column=2)

Add=Button(a,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="+",bg="sky blue",command=lambda:laxClick("+")).grid(row=3,column=3)

Mod=Button(a,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="%",bg="sky blue",command=lambda:laxClick("%")).grid(row=4,column=0)

lax=Button(a,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="0",bg="sky blue",command=lambda:laxClick(0)).grid(row=4,column=1)

Add=Button(a,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="+",bg="sky blue",command=lambda:laxClick("+")).grid(row=4,column=2)

Equal=Button(a,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="=",bg="sky blue",command=laxEqualsInput).grid(row=4,column=3)

Clear=Button(a,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="C",bg="sky blue",command=laxClearDis).grid(row=5,column=0)

Div=Button(a,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="/",bg="sky blue",command=lambda:laxClick("/")).grid(row=5,column=1)

Exp=Button(a,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="**",bg="sky blue",command=lambda:laxClick("**")).grid(row=5,column=2)

float=Button(a,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text=".",bg="sky blue",command=lambda:laxClick(".")).grid(row=5,column=3)

a.mainloop()