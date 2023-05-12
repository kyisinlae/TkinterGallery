import tkinter as tk
from tkinter import *

window = Tk()

Label(window, text ='Foods to choose.', font="Tahoma 15").place(x = 20, y = 10)
 
pizza = Checkbutton(window, text ='Pizza', font="Tahoma 15",
                takefocus = 0).place(x = 40, y = 40)

apple = Checkbutton(window, text ='Apple', font="Tahoma 15",
                takefocus = 0).place(x = 40, y = 90)

chocolate = Checkbutton(window, text ='Chocolate', font="Tahoma 15",
                takefocus = 0).place(x = 40, y = 140)

cookie = Checkbutton(window, text ='Cookie', font="Tahoma 15",
                takefocus = 0).place(x = 40, y = 190)

Label(window, text='Drinks to choose.', font="Tahoma 15").place(x = 260, y=10)

lemonade = Checkbutton(window, text='Lemonade', font="Tahoma 15",
                takefocus= 0).place(x=280, y=40)

applejuice = Checkbutton(window, text='Apple Juice', font="Tahoma 15",
                takefocus = 0).place(x=280, y=90)

bubbletea = Checkbutton(window, text='Bubble Tea', font="Tahoma 15",
                takefocus = 0).place(x=280, y=140)

milk = Checkbutton(window, text='Milk', font="Tahoma 15",
                takefocus = 0).place(x=280, y=190)

window.mainloop()