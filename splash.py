import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

def show_splash(root):
    splash = Toplevel(root)
    window_height = 300
    window_width = 600
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    splash.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    frame = tk.Frame(splash, background="#f0f0f0", height= 20)
    
    frame1 = tk.Frame(frame, background="#f0f0f0", width=200)
    frame2 = tk.Frame(frame, background="#f0f0f0")

    frame3 = tk.Frame(frame1, background="#f0f0f0", height= 150, width=150, padx=10,pady=10)
    frame3.place(in_=frame1, anchor="center",  relx=.5, rely=.5)
    
    image = Image.open("./images/tklogo1.png")
    
    resized_image= image.resize((150,150))
    img= ImageTk.PhotoImage(resized_image)

    Label(frame3, image=img).pack()

    
    frame4 = Frame(frame2, background="#f0f0f0", height=50)
    frame5 = Frame(frame2, background="#f0f0f0")
    frame6 = Frame(frame2, background="#f0f0f0", height=50)
    
    
    frame4.pack(side="top", fill="x")
    frame5.pack(side="top", fill="both", expand=True)
    frame6.pack(side="bottom", fill="x")
    
    apptitle = Label(frame5, text='Tkinter Gallery', font="Helvetica 25 bold", padx=10,pady=10)
    apptitle.pack(side=TOP, anchor=W)
    
    appdescription = Label(frame5, text='This is about tkinter, for basic learners.', font="Tahoma 10", padx=10,pady=10)
    appdescription.pack(side=TOP, anchor=W)
    
    apppowerby = Label(frame6, text='Power by KSL and TKPK from LTE PY4Y B8', font="Tahoma 7", padx=10,pady=10)
    apppowerby.pack(side=BOTTOM, anchor=W)

    frame1.pack(side="left", fill="y")
    frame2.pack(side="right", fill="both", expand=True)
    
    
    
    frame.pack(side="top", fill="both", expand=True)
    splash.overrideredirect(True)
    splash.after(2000, splash.destroy)
    splash.wait_window()
    

    