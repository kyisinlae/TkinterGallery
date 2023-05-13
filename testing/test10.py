import tkinter as tk
from tkinter import ttk
from tkinter import *
import pyperclip as pc

window = Tk()
scroll_v = tk.Scrollbar(window)
scroll_v.pack(side= tk.RIGHT,fill=tk.Y)
#Add a Horizontal Scrollbar
scroll_h = tk.Scrollbar(window, orient= HORIZONTAL)
scroll_h.pack(side= tk.BOTTOM, fill= tk.X)

window.mainloop()