# import tkinter
# top=tkinter.Tk()
# # code to add widgets will here....
# Top. mainloop()

from tkinter import*

def btnClick(numbers):
    global operator
    operator=operator+str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator=""
    text_Input.set("")

def btnEqualsInput():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator=""

cal = Tk()
cal.title("Calculator")
operator=""
text_Input =StringVar()

txtDisplay = Entry(cal,font=('arial', 20,'bold'),textvariable=text_Input, bd=30,insertwidth=4, bg="silver", justify="right").grid(columnspan=4)

btn7=Button(cal,padx=16, pady=16,bd=8, fg="black",font=('arial', 20,'bold'),text="7", bg="pink",command=lambda:btnClick(7)).grid(row=1,column=0)

btn8=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial', 20,'bold'),text="8", bg="pink",command=lambda:btnClick(8)).grid(row=1,column=1)

btn9=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial', 20,'bold'),text="9", bg="pink",command=lambda:btnClick(9)).grid(row=1,column=2)

addition=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial', 20,'bold'),text="+", bg="pink",command=lambda:btnClick("+")).grid(row=1,column=3)


btn4=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial', 20,'bold'),text="4", bg="pink",command=lambda:btnClick(4)).grid(row=2,column=0)

btn5=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial', 20,'bold'),text="5", bg="pink",command=lambda:btnClick(5)).grid(row=2,column=1)

btn6=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial', 20,'bold'),text="6", bg="pink",command=lambda:btnClick(6)).grid(row=2,column=2)

subcration=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial', 20,'bold'),text="-", bg="pink",command=lambda:btnClick("-")).grid(row=2,column=3)


btn1=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial', 20,'bold'),text="1", bg="pink",command=lambda:btnClick(1)).grid(row=3,column=0)

btn2=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial', 20,'bold'),text="2", bg="pink",command=lambda:btnClick(2)).grid(row=3,column=1)

btn3=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial', 20,'bold'),text="3", bg="pink",command=lambda:btnClick(3)).grid(row=3,column=2)

multiply=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial', 20,'bold'),text="*", bg="pink",command=lambda:btnClick("*")).grid(row=3,column=3)


Clear=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial', 20,'bold'),text="C", bg="pink",command=btnClearDisplay).grid(row=4,column=0)

btn0=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial', 20,'bold'),text="0", bg="pink",command=lambda:btnClick(0)).grid(row=4,column=1)

Equal=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial', 20,'bold'),text="=", bg="pink",command=btnEqualsInput).grid(row=4,column=2)

Divsion=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial', 20,'bold'),text="/", bg="pink",command=lambda:btnClick("/")).grid(row=4,column=3)

cal.mainloop() 