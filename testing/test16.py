
from tkinter import *
from tkinter import colorchooser
from tkinter import messagebox
 
root = Tk()
root.geometry("300x300")

def choose_color():
    color_code = colorchooser.askcolor(title ="Choose color")
    # print(color_code)
    messagebox.showinfo("Color Code", color_code)
    
button = Button(root, text = "Select color", command = choose_color)
button.pack()

root.mainloop()