import tkinter as tk
from tkinter import ttk
from tkinter import *

def openAbout(root):
    entryWindow = tk.Toplevel(root)
    entryWindow.title("About")
    window_height = 300
    window_width = 600
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    entryWindow.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    frame = tk.Frame(entryWindow)
    frame.pack()
    entryWindow.resizable(False, False)
#     root.mainloop()