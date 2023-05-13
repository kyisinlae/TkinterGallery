from tkinter import *
from PIL import ImageTk,Image


ws = Tk()
ws.title('Image')
ws.geometry ('500x500')
ws.config(bg="black")
Label(ws, text='width',width=8).place(x=0,y=0)
width=Entry(ws,width=10)
width.insert(END,300)
width.place(x=80,y=0)
Label(ws,text='Height',width=8).place(x=0,y=20)
height=Entry(ws,width=10)
height.insert(END,350)
height.place(x=80,y=20)
resize_button=Button(ws,text="ok")
resize_button.place(x=50,y=50)
ws.mainloop()