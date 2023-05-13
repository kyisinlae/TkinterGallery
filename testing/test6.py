import tkinter as tk
from tkinter import *

window = Tk()

def greet():
    name = "Hello " + my_text_box.get()
    name_label.config(text=name, font="Tahoma20")
def welcome():
    name = "Welcome "
    name_label.config(text=name, font="Tahoma20")
    
name_label = tk.Label(window, text=" ")
name_label.grid(row=1, column=1)

my_text_box = tk.Entry(window, width=40, font="Tahoma20")
my_text_box.grid(row=0, column=2)
my_button = tk.Button(window, text = "Hello!", font="Tahoma20" , command=greet)
my_button.grid(row=1, column=2)

my_button = tk.Button(window, text = "Welcome!", font="Tahoma20" , command=welcome)
my_button.grid(row=2, column=2)

window.mainloop()
