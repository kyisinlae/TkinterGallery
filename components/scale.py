import tkinter as tk
from tkinter import ttk
from tkinter import *
import pyperclip as pc

def openScale(root):
    
    for widget in root.winfo_children():
        if isinstance(widget, ttk.PanedWindow):
            widget.destroy()

    panedwindow=ttk.Panedwindow(root, orient=HORIZONTAL)
    panedwindow.pack(fill=BOTH, expand=True)
    # formView=ttk.Frame(panedwindow,width=100,height=300, relief=SUNKEN)  
    # codeView=ttk.Frame(panedwindow,width=400,height=400, relief=SUNKEN)
    formView=ttk.Frame(panedwindow, relief=SUNKEN)  
    codeView=ttk.Frame(panedwindow, width=100,relief=SUNKEN)
    formtitle=tk.Frame(formView, background="white")
    formtitle.pack(side="top", fill="x", anchor="center")
    formlable = tk.Label(formtitle,text="Scale", font="Tahoma 15", height=1, bg="white", pady=5)
    formlable.pack(side="top", anchor="center")
    formdesigner = tk.Frame(formView, background="white", padx=10,pady=10)
    formdesigner.pack(side="top", fill="both", expand=True)
    
    panedwindow.add(formView, weight=5)  
    panedwindow.add(codeView, weight=2)
    
    length_label = Label(formdesigner, text='').grid(row=0, column=0, pady=4, padx = 4)
    w2 = Scale(formdesigner, from_=0, to=100, tickinterval= 100, orient=HORIZONTAL, length=400)
    w2.set(50)
    w2.grid(row=0, column=1)

    mainframe = ttk.Frame(formdesigner, padding="24 24 24 24")
    mainframe.grid(column=1, row=1, sticky=(N, W, E, S))
    slider = IntVar()
    ttk.Scale(mainframe, from_=0, to_=100, length=300,  variable=slider).grid(column=1, row=4, columnspan=5)
    ttk.Label(mainframe, textvariable=slider).grid(column=1, row=0, columnspan=5)
    for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
    0000000
    scroll_v = tk.Scrollbar(codeView)
    scroll_v.pack(side= tk.RIGHT,fill=tk.Y)

    #Add a Horizontal Scrollbar
    scroll_h = tk.Scrollbar(codeView, orient= HORIZONTAL)
    scroll_h.pack(side= tk.BOTTOM, fill= tk.X)
    #Add a Text widget
    text = Text(codeView, width=45, yscrollcommand= scroll_v.set, xscrollcommand = scroll_h.set, wrap= NONE, font= ('Consolas 11'))
    text.pack(fill="both", expand=True)
    
    
     #Attact the scrollbar with the text widget
    scroll_h.config(command = text.xview)
    scroll_v.config(command = text.yview)
    
    insert_text = """
    
    
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
    """
    
    text.insert(tk.END, insert_text)
    
    def clickCopyCode():
        pc.copy(insert_text)
        # a = pc.paste()
        # print(a)
    
    
    # ttk.Button(codeView, text="Close", command=panedwindow.destroy).grid(column=2, row=0)
    # ttk.Button(codeView, text="Copy Code", command=panedwindow.destroy).grid(column=1, row=0)
    ttk.Button(codeView, text="Close", command=panedwindow.destroy).place(x=10, y=10)
    ttk.Button(codeView, text="Copy Code", command=clickCopyCode).place(x=90, y=10)