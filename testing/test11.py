import tkinter as tk
from tkinter import *

window = Tk()

number = tk.Label(window, text= "Age", font="Tahoma 15")
number_spinbox = tk.Spinbox(window, from_=1, to=100, font="Tahoma 15")
number.grid(row=1, column=1)
number_spinbox.grid(row=2, column=1)

my_list=['One', 'Two', 'Three', 'Four', 'Five']
sb2 = Spinbox(window,values=my_list,width=10, font="Tahoma 15")
sb2.grid(row=2,column=2,padx=20,pady=20)

window.mainloop()