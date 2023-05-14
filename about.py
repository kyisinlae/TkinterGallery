import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

def openAbout(root):
    aboutWindow = Toplevel(root)
    aboutWindow.title("About")
    window_height = 300
    window_width = 600
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    aboutWindow.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    # aboutWindow.wm_attributes("-transparentcolor", '#f0f0f0')
    
    frame = tk.Frame(aboutWindow, background="#f0f0f0")
    frame.pack(fill="both", expand=True)
    
    frame1 = tk.Frame(frame, background="#f0f0f0", height=50)
    frame1.pack(side="bottom", fill="x")
    
    frame2 = tk.Frame(frame, background="#f0f0f0", width=400)    
    frame2.pack(side="left", fill="y", padx = 10, pady = 10)
    
    frame3 = tk.Frame(frame, background="#f0f0f0")
    frame3.pack(fill="both", expand=True)
    
    
    frame4 = Frame(frame3,background="#f0f0f0", width=150, height=150, border=0)
    frame4.pack(side='top', anchor="se", padx = 10, pady = 10)

    image = Image.open("./images/tklogo1.png")
    resized_image= image.resize((150,150))
    img= ImageTk.PhotoImage(resized_image)
    logoimage = tk.Label(frame4, image=img,relief=GROOVE)
    logoimage.pack()
    # logoimage.draw()
    
    
    apptitle = Label(frame2, text='Tkinter Gallery', font="Helvetica 25 bold", padx=10,pady=10)
    apptitle.pack(side=TOP, anchor=W)
    
    appdescription = Label(frame2, text='This is about tkinter, for basic learners.', font="Tahoma 10", padx=10,pady=10)
    appdescription.pack(side=TOP, anchor=W)
    
    apppowerby = Label(frame1, text='Power by KSL and TKPK from LTE PY4Y B8', font="Tahoma 7", padx=10,pady=10)
    apppowerby.pack(side=BOTTOM, anchor='center')
    
   
   
    aboutWindow.resizable(False, False)
    # # entryWindow.attributes("-toolwindow", True)
    # # entryWindow.overrideredirect(1)
    # # entryWindow.transient(1)
    
    aboutWindow.mainloop()