from operator import add
from tkinter import *
from turtle import clear


def btnClick(numbers):
    global operator
    operator=operator + str(numbers)
    data.set(operator)

def btnClearDisplay():
    global operator
    operator=""
    data.set("")

def btnEqualsInput():
    global operator
    sumup=str(eval(operator))
    data.set(sumup)
 
def btnsquare():
       result = str(eval(operator))
       squared_result = float(result) ** 2
       data.set(str(squared_result))
       
def btnDel():
     global operator
     operator = operator[:-1] 
     data.set(operator)
       
def btnSqrt():
    global operator  
    result = str(eval(operator))
    sqrt_result =(float(result))**0.5
    data.set(str(sqrt_result))
    operator = str(sqrt_result)

def btnreciprocal():
    global operator
    result = str(eval(operator))
    reciprocal_result = 1 / float(result)
    data.set(str(reciprocal_result))
    operator = str(reciprocal_result)

def btnCuberoot():
    global operator
    result = str(eval(operator))
    cube_root_result = float(result) ** (1/3)
    data.set(str(cube_root_result))
    operator = str(cube_root_result)


def btnMemorySave():
    global operator, memory
    memory = float(eval(operator))
    data.set("Memory Saved")

def btnMemoryRecall():
    global operator, memory
    data.set(str(memory))
    operator = str(memory)

def btnMemoryClear():
    global operator, memory
    memory= None
    data.set(" ")

def btnExponent():
    global operator
    operator += "**"
    data.set(operator)

def btnPercentage():
    global operator
    result = str(eval(operator) / 100)
    data.set(result)
    operator = result
 



root = Tk()
root.title("Mahak's calci")
root.geometry("330x470+500+200")
operator=""
data=StringVar()
display=Entry(root, textvariable=data, bd=20, justify="right", bg="white", font=("ariel",20))
display.grid(row=0,columnspan=18)

btn7=Button(root,text="7",font=("Ariel",10,"bold"),bg="powder blue",bd=12,height=2,width=4,command=lambda:btnClick(7))
btn7.grid(row=1,column=0)

btn8=Button(root,text="8",font=("Ariel",10,"bold"),bg="powder blue",bd=12,height=2,width=4,command=lambda:btnClick(8))
btn8.grid(row=1,column=1)

btn9=Button(root,text="9",font=("Ariel",10,"bold"),bg="powder blue",bd=12,height=2,width=4,command=lambda:btnClick(9))
btn9.grid(row=1,column=2)

btn_add=Button(root,text="+",font=("Ariel",10,"bold"),bg="powder blue",bd=12,height=2,width=4,command=lambda:btnClick("+"))
btn_add.grid(row=1,column=3)

btn_clear=Button(root,text="C",font=("Ariel",10,"bold"),bg="powder blue",bd=12,height=2,width=4,command=lambda:btnClearDisplay())
btn_clear.grid(row=1,column=4)

btn4=Button(root,text="4",font=("Ariel",10,"bold"),bg="powder blue",bd=12,height=2,width=4,command=lambda:btnClick(4))
btn4.grid(row=2,column=0)

btn5=Button(root,text="5",font=("Ariel",10,"bold"),bg="powder blue",bd=12,height=2,width=4,command=lambda:btnClick(5))
btn5.grid(row=2,column=1)

btn6=Button(root,text="6",font=("Ariel",10,"bold"),bg="powder blue",bd=12,height=2,width=4,command=lambda:btnClick(6))
btn6.grid(row=2,column=2)

btn_sub=Button(root,text="-",font=("Ariel",10,"bold"),bg="powder blue",bd=12,height=2,width=4,command=lambda:btnClick("-"))
btn_sub.grid(row=2,column=3)

btn_perc=Button(root,text="%",font=("Ariel",10,"bold"),bg="powder blue",bd=12,height=2,width=4,command=lambda:btnPercentage())
btn_perc.grid(row=2,column=4)

btn1=Button(root,text="1",font=("Ariel",10,"bold"),bg="powder blue",bd=12,height=2,width=4,command=lambda:btnClick(1))
btn1.grid(row=3,column=0)

btn2=Button(root,text="2",font=("Ariel",10,"bold"),bg="powder blue",bd=12,height=2,width=4,command=lambda:btnClick(2))
btn2.grid(row=3,column=1)

btn3=Button(root,text="3",font=("Ariel",10,"bold"),bg="powder blue",bd=12,height=2,width=4,command=lambda:btnClick(3))
btn3.grid(row=3,column=2)

btn_mult=Button(root,text="*",font=("Ariel",10,"bold"),bg="powder blue",bd=12,height=2,width=4,command=lambda:btnClick("*"))
btn_mult.grid(row=3,column=3)

btn_div=Button(root,text="/",font=("Ariel",10,"bold"),bg="powder blue",bd=12,height=2,width=4,command=lambda:btnClick("/"))
btn_div.grid(row=4,column=3)

btn_square=Button(root,text="x2",font=("Ariel",10,"bold"),bg="powder blue",bd=12,height=2,width=4,command=lambda: btnsquare())
btn_square.grid(row=4,column=4)

btn_leftbracket=Button(root,text="(",font=("Ariel",10,"bold"),bg="powder blue",bd=12,height=2,width=4,command=lambda:btnClick("("))
btn_leftbracket.grid(row=4,column=0)

btn0=Button(root,text="0",font=("Ariel",10,"bold"),bg="powder blue",bd=12,height=2,width=4,command=lambda:btnClick(0))
btn0.grid(row=4,column=1)

btn_rightbracket=Button(root,text=")",font=("Ariel",10,"bold"),bg="powder blue",bd=12,height=2,width=4,command=lambda:btnClick(")"))
btn_rightbracket.grid(row=4,column=2)

btn_point=Button(root,text=".",font=("Ariel",10,"bold"),bg="powder blue",bd=12,height=2,width=4,command=lambda:btnClick("."))
btn_point.grid(row=3,column=4)

btn_del=Button(root,text="DEL",font=("Ariel",10,"bold"),bg="powder blue",bd=12,height=2,width=4,command=lambda:btnDel())
btn_del.grid(row=5,column=3)

btn_equal=Button(root,text="=",font=("Ariel",10,"bold"),bg="powder blue",bd=12,height=2,width=4,command=lambda:btnEqualsInput())
btn_equal.grid(row=5,column=4)

btn_sqrt = Button(root, text="√", font=("Ariel", 10, "bold"), bg="powder blue", bd=12, height=2, width=4, command=lambda:btnSqrt())
btn_sqrt.grid(row=5, column=2)

btn_reciprocal = Button(root, text="1/x", font=("Ariel", 10, "bold"), bg="powder blue", bd=12, height=2, width=4, command=lambda:btnreciprocal())
btn_reciprocal.grid(row=5, column=1)

btn_cuberoot = Button(root, text="∛", font=("Ariel", 10, "bold"), bg="powder blue", bd=12, height=2, width=4, command=lambda:btnCuberoot())
btn_cuberoot.grid(row=5, column=0)

btn_memorysave = Button(root, text="MS", font=("Ariel", 10, "bold"), bg="powder blue", bd=12, height=2, width=4, command=lambda:btnMemorySave())
btn_memorysave.grid(row=6, column=0)

btn_memoryrecall = Button(root, text="MR", font=("Ariel", 10, "bold"), bg="powder blue", bd=12, height=2, width=4, command=lambda:btnMemoryRecall())
btn_memoryrecall.grid(row=6, column=1)

btn_memoryclear = Button(root, text="MC", font=("Ariel", 10, "bold"), bg="powder blue", bd=12, height=2, width=4, command=lambda:btnMemoryClear())
btn_memoryclear.grid(row=6, column=2)

btn_exponentiation = Button(root, text="^", font=("Ariel", 10, "bold"), bg="powder blue", bd=12, height=2, width=4, command=lambda:btnExponent())
btn_exponentiation.grid(row=6, column=3)

btn_00 = Button(root, text="00", font=("Ariel", 10, "bold"), bg="powder blue", bd=12, height=2, width=4, command=lambda:btnClick("00"))
btn_00.grid(row=6, column=4)






root.mainloop()