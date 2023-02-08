import tkinter as tk
win=tk.Tk()
win.title('Thambola Ticket')

canvas=tk.Canvas(win,width=400,height=400)
x1=100
x2=130
y1=100
y2=130

num=1
for i in range(9):
    for i in range(3):
        canvas.create_rectangle(x1,y1,x2,y2,outline='blue',fill='orange')
        lab=tk.Label(canvas,text=str(num),font='Arial 10 bold',bg='light blue')
        num=num+1
        y1=y1+30
        y2=y2+30
        y1=100
        y2=130
        x1=x1+30
        x2=x2+30
canvas.pack()
win.mainloop()
