import tkinter as tk
from tkinter import ttk
from tkinter import *
import pyperclip as pc

def openTab(root):
    
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
    formlable = tk.Label(formtitle,text="Radio Button", font="Tahoma 15", height=1, bg="white", pady=5)
    formlable.pack(side="top", anchor="center")
    formdesigner = tk.Frame(formView, background="white", padx=10,pady=10)
    formdesigner.pack(side="top", fill="both", expand=True)
    
    panedwindow.add(formView, weight=5)  
    panedwindow.add(codeView, weight=2)
    
    tabControl = ttk.Notebook(formdesigner)
  
    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)
    
    tabControl.add(tab1, text ='Tab 1')
    tabControl.add(tab2, text ='Tab 2')
    tabControl.pack(expand = 1, fill ="both")
    
    ttk.Label(tab1, text ="Welcome to Tkinter Gallery").grid(column = 0, row = 0,padx = 30,pady = 30)  
    ttk.Label(tab2,text ="Lets go into the \
        world of computers").grid(column = 0,row = 0, padx = 30,pady = 30)
    
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
    
    
    window = tk.Tk()
    tabControl = ttk.Notebook(window)
    
    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)
    
    tabControl.add(tab1, text ='Tab 1')
    tabControl.add(tab2, text ='Tab 2')
    tabControl.pack(expand = 1, fill ="both")
    
    ttk.Label(tab1, text ="Welcome to Tkinter Gallery").grid(column = 0, row = 0,padx = 30,pady = 30)  
    ttk.Label(tab2,text ="Lets go into the \
        world of computers").grid(column = 0,row = 0, padx = 30,pady = 30)

    window.mainloop()  
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