import tkinter as tk
from tkinter import ttk
from tkinter import *

def openFrameLayout(root):
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
    ttk.Button(frm, text="Remove", command=frm.destroy).grid(column=1, row=0)
    root.mainloop()