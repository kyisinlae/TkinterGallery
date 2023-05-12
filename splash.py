from tkinter import *

def show_splash(root):
    splash = Toplevel(root)
    window_height = 300
    window_width = 600
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    splash.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    frame = Frame(splash)
    frame.pack()
    splash.overrideredirect(True)
    splash.after(1000, splash.destroy)
    splash.wait_window()
