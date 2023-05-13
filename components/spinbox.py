import tkinter as tk
from tkinter import ttk
from tkinter import *
import pyperclip as pc

def openSpinBox(root):
    
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
    formlable = tk.Label(formtitle,text="Spin Box", font="Tahoma 15", height=1, bg="white", pady=5)
    formlable.pack(side="top", anchor="center")
    formdesigner = tk.Frame(formView, background="white", padx=10,pady=10)
    formdesigner.pack(side="top", fill="both", expand=True)
    
    panedwindow.add(formView, weight=5)  
    panedwindow.add(codeView, weight=2)
    
    number = tk.Label(formdesigner, text= "Age", font="Tahoma 15")
    number_spinbox = tk.Spinbox(formdesigner, from_=1, to=100, font="Tahoma 15")
    number.grid(row=1, column=1)
    number_spinbox.grid(row=2, column=1)
    
    my_list=['One', 'Two', 'Three', 'Four', 'Five']
    sb2 = Spinbox(formdesigner,values=my_list,width=10, font="Tahoma 15")
    sb2.grid(row=2,column=2,padx=20,pady=20)
        
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
    from tkinter import *

    window = tk.Tk()
    labeltitle=tk.Label(text="Welcome!", bg="white",fg="blue", font="Consolas 11")
    labeltitle.pack(side="top", fill="both", anchor="w")    
    label1=tk.Label(text="This is a label.", bg="white",fg="black", font="Consolas 11")
    label1.pack(side="top", fill="both", anchor="w")
    label2=tk.Label(text="We can change the font style.", bg="white",fg="black", font=("arial italic", 11) )
    label2.pack(side="top", fill="both", anchor="w")
    label3=tk.Label(text="This is a disable label.", bg="white", fg="black", font="Consolas 11", state='disabled')
    label3.pack(side="top", fill="both", anchor="w")
    label4=tk.Label(text="This is a normal label.", bg="white", fg="black", font="Consolas 11")
    label4.pack(side="top", fill="both", anchor="w")
    label5=tk.Label(text="We can also change the font color.", bg="white", fg="red", font="Consolas 11")
    label5.pack(side="top", fill="both", anchor="w")

    Label(window, text="Flat border", borderwidth=3, relief="flat", padx=5, pady=10).pack(padx=5, pady=10)
    Label(window, text="raised border", borderwidth=3, relief="raised", padx=5, pady=10).pack(padx=5, pady=10)
    Label(window, text="sunken border", borderwidth=3, relief="sunken", padx=5, pady=10).pack(padx=5, pady=10)
    Label(window, text="ridge border", borderwidth=3, relief="ridge", padx=5, pady=10).pack(padx=5, pady=10)
    Label(window, text="solid border", borderwidth=3, relief="solid", padx=5, pady=10).pack(padx=5, pady=10)
    Label(window, text="groove border", borderwidth=3, relief="groove",padx=5, pady=10).pack(padx=5, pady=10)

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