import tkinter as tk
from tkinter import ttk
from tkinter import *
import pyperclip as pc

def openCombobox(root):
    
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
    formlable = tk.Label(formtitle,text="Combobox", font="Tahoma 15", height=1, bg="white", pady=5)
    formlable.pack(side="top", anchor="center")
    formdesigner = tk.Frame(formView, background="white", padx=10,pady=10)
    formdesigner.pack(side="top", fill="both", expand=True)
    
    panedwindow.add(formView, weight=5)  
    panedwindow.add(codeView, weight=2)
    
    nationality = tk.Label(formdesigner, text="Nationality", font="Tahoma 15")
    nationality_combobox = ttk.Combobox(formdesigner, values=["America", "Myanmar", "China", "Africa", "Thailand", "India"], font="Tahoma 15")
    nationality.grid(row=2, column=0)
    nationality_combobox.grid(row=3, column=0)

    title = tk.Label(formdesigner, text= "Title", font="Tahoma 15")
    title_combobox = ttk.Combobox(formdesigner, values=["Mr.", "Ms."], font="Tahoma 15")
    title.grid(row=2, column=2)
    title_combobox.grid(row=3, column=2)
    bdmonth = tk.Label(formdesigner,text="Birthday Month", font="Tahoma 15")
    bdmonth_combobox = ttk.Combobox(formdesigner, values=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November","December"], font="Tahoma 15")
    bdmonth.grid(row=2, column=3)
    bdmonth_combobox.grid(row=3, column=3)
    
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

    window = Tk()

    nationality = tk.Label(window, text="Nationality", font="Tahoma 15")
    nationality_combobox = ttk.Combobox(window, values=["America", "Myanmar", "China", "Africa", "Thailand", "India"], font="Tahoma 15")
    nationality.grid(row=2, column=0)
    nationality_combobox.grid(row=3, column=0)
    title = tk.Label(window, text= "Title", font="Tahoma 15")
    title_combobox = ttk.Combobox(window, values=["Mr.", "Ms."], font="Tahoma 15")
    title.grid(row=2, column=2)
    title_combobox.grid(row=3, column=2)
    bdmonth = tk.Label(window,text="Birthday Month", font="Tahoma 15")
    bdmonth_combobox = ttk.Combobox(window, values=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November","December"], font="Tahoma 15")
    bdmonth.grid(row=2, column=3)
    bdmonth_combobox.grid(row=3, column=3)
        

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