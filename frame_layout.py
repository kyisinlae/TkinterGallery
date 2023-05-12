import tkinter as tk
from tkinter import ttk
from tkinter import *
import pyperclip as pc

def openFrameLayout(root):
    # print(root.winfo_children())
    for widget in root.winfo_children():
        if isinstance(widget, ttk.PanedWindow):
            widget.destroy()
            # widget.delete(0, "end")
    
    panedwindow=ttk.Panedwindow(root, orient=HORIZONTAL)
    panedwindow.pack(fill=BOTH, expand=True)
    # formView=ttk.Frame(panedwindow,width=100,height=300, relief=SUNKEN)  
    # codeView=ttk.Frame(panedwindow,width=400,height=400, relief=SUNKEN)
    formView=ttk.Frame(panedwindow, relief=SUNKEN)  
    codeView=ttk.Frame(panedwindow, width=50,relief=SUNKEN)
    
    formtitle=tk.Frame(formView, background="white")
    formtitle.pack(side="top", fill="x", anchor="center")
    formlable = tk.Label(formtitle,text="Frame Layout", font="Tahoma 15", height=1, bg="white", pady=5)
    formlable.pack(side="top", anchor="center")
    formdesigner = tk.Frame(formView, background="white", padx=10,pady=10)
    formdesigner.pack(side="top", fill="both", expand=True)
    
    # // FormDesigner Start .... 
    
    toolbar = tk.Frame(formdesigner, background="yellow", height=40)
    statusbar = tk.Frame(formdesigner, background="red", height=20)
    main = tk.Frame(formdesigner, background="green", height=20)


    toolbar.pack(side="top", fill="x")
    statusbar.pack(side="bottom", fill="x")
    main.pack(side="top", fill="both", expand=True)

    left_pane = tk.Frame(main, background="pink", width=100)
    right_pane = tk.Frame(main, background="cyan", width=200)

    left_pane.pack(side="left", fill="y")
    right_pane.pack(side="right", fill="y")

    custom_pane = tk.Frame(main, background="orange", height=200, width=200)
    custom_pane.pack(side="bottom", anchor="se") # // n, ne, e, se, s, sw, w, nw, or center
    
    # // FormDesigner End .... 
    
    
    
    # // CodeView Start .... 
     
    # text = tk.Text(codeView)
    # scroll = tk.Scrollbar(text)
    # text.configure(yscrollcommand=scroll.set)
    # text.pack(side="top", fill="both", expand=True)
    # scroll.config(command=text.yview)
    # scroll.pack(side=tk.RIGHT, fill=tk.Y)
    
    
    text = tk.Text(codeView)
    

   
    #Add a Vertical Scrollbar
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

    root = tk.Tk()
    root.geometry("600x400")

    toolbar = tk.Frame(root, background="yellow", height=40)
    statusbar = tk.Frame(root, background="red", height=20)
    main = tk.Frame(root, background="green", height=20)


    toolbar.pack(side="top", fill="x")
    statusbar.pack(side="bottom", fill="x")
    main.pack(side="top", fill="both", expand=True)

    left_pane = tk.Frame(main, background="pink", width=100)
    right_pane = tk.Frame(main, background="cyan", width=200)

    left_pane.pack(side="left", fill="y")
    right_pane.pack(side="right", fill="y")

    custom_pane = tk.Frame(main, background="orange", height=200, width=200)
    custom_pane.pack(side="bottom", anchor="se") # // n, ne, e, se, s, sw, w, nw, or center

    root.mainloop()
    """
    
    text.insert(tk.END, insert_text)
   
    # // CodeView End .... 
    
    
    panedwindow.add(formView, weight=40)  
    panedwindow.add(codeView, weight=1)
    
    
    def clickCopyCode():
        pc.copy(insert_text)
        # a = pc.paste()
        # print(a)
    
    # ttk.Button(codeView, text="Close", command=panedwindow.destroy).grid(column=2, row=0)
    # ttk.Button(codeView, text="Copy Code", command=panedwindow.destroy).grid(column=1, row=0)
    ttk.Button(codeView, text="Close", command=panedwindow.destroy).place(x=10, y=10)
    ttk.Button(codeView, text="Copy Code", command=clickCopyCode).place(x=90, y=10)
    
