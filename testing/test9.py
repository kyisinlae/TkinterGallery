import tkinter as tk
from tkinter import ttk
from tkinter import *

root = Tk()

length_label = Label(root, text='').grid(row=0, column=0, pady=4, padx = 4)
w2 = Scale(root, from_=0, to=100, tickinterval= 100, orient=HORIZONTAL, length=400)
w2.set(50)
w2.grid(row=0, column=1)

mainframe = ttk.Frame(root, padding="24 24 24 24")
mainframe.grid(column=1, row=1, sticky=(N, W, E, S))
slider = IntVar()
ttk.Scale(mainframe, from_=0, to_=100, length=300,  variable=slider).grid(column=1, row=4, columnspan=5)
ttk.Label(mainframe, textvariable=slider).grid(column=1, row=0, columnspan=5)
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
0000000

root.mainloop()