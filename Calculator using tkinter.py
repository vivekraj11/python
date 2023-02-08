import tkinter as tk

def add():
    tk.Label(win,text="Result").grid(row=3,column=0)
    tk.Label(win,text=str(int(e1.get())+int(e2.get()))).grid(row=3,column=1)

def Mul():
     tk.Label(win,text="Result").grid(row=3,column=0)
     tk.Label(win,text=str(int(e1.get())*int(e2.get()))).grid(row=3,column=4)

def subs():
     tk.Label(win,text="Result").grid(row=3,column=0)
     tk.Label(win,text=str(int(e1.get())-int(e2.get()))).grid(row=3,column=2)

def Div():
     tk.Label(win,text="Result").grid(row=3,column=0)
     tk.Label(win,text=str(int(e1.get())/int(e2.get()))).grid(row=3,column=3)
win=tk.Tk()
win.title("Calculator")
canvas=tk.Canvas(win,width='600',height='600')
tk.Label(win,text="operand 1",font="Arial 12 bold").grid(row=0,padx=10,pady=10)
tk.Label(win,text="operand 2",font="Arial 12 bold").grid(row=1,padx=10,pady=10)
e1=tk.Entry(win,fg="black",bg="yellow")
e2=tk.Entry(win,fg="black",bg="yellow")
e1.grid(row=0,column=1,padx=10,pady=10)
e2.grid(row=1,column=1,padx=10,pady=10)

tk.Button(win,text="Addition", command=add,font="Arial 12 bold",fg="yellow",bg="cyan").grid(row=5,column=1,padx=10,pady=10)
tk.Button(win,text="Subtraction", command=subs,font="Arial 12 bold",fg="yellow",bg="cyan").grid(row=5,column=2,padx=10,pady=10)
tk.Button(win,text="Division", command=Div,font="Arial 12 bold",fg="yellow",bg="cyan").grid(row=5,column=3,padx=10,pady=10)
tk.Button(win,text="Multiplication", command=Mul,font="Arial 12 bold",fg="yellow",bg="cyan").grid(row=5,column=4,padx=10,pady=10)

def quits():
    win.destroy()
tk.Button(win,text="Exit", command=quits,font="Arial 12 bold",fg="white",bg="red").grid(row=5,column=0,padx=10,pady=10)

