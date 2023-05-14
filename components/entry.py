import tkinter as tk
from tkinter import ttk
from tkinter import *
import pyperclip as pc

def openEntryForm(root):
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
    codeView=ttk.Frame(panedwindow, width=100,relief=SUNKEN)
    
    panedwindow.add(formView, weight=5)  
    panedwindow.add(codeView, weight=2)
    
    formtitle=tk.Frame(formView, background="white")
    formtitle.pack(side="top", fill="x", anchor="center")
    formlable = tk.Label(formtitle,text="Entry", font="Tahoma 20", height=1, bg="white", pady=5)
    formlable.pack(side="top", anchor="center")
    formdesigner = tk.Frame(formView, background="#DFDFDF", padx=10,pady=10)
    formdesigner.pack(side="top", fill="both", expand=True)
        
    firstname = tk.Label(formdesigner, text= "First name", font="Tahoma 15")
    firstname.grid(row=0, column=0, padx=10,pady=10)

    lastname = tk.Label(formdesigner, text="Last name", font="Tahoma 15")
    lastname.grid(row=0, column=1, padx=10,pady=10)

    nickname = tk.Label(formdesigner, text = "Nick name", font="Tahoma 15")
    nickname.grid(row=0, column=2, padx=10,pady=10)

    firstname = tk.Entry(formdesigner, font="Tahoma 15")
    lastname = tk.Entry(formdesigner, font="Tahoma 15")
    nickname = tk.Entry(formdesigner, font="Tahoma 15")
  
    firstname.grid(row=1, column=0, padx=10,pady=10)
    lastname.grid(row=1, column=1, padx=10,pady=10)
    nickname.grid(row=1, column=2, padx=10,pady=10)
    
    age = tk.Label(formdesigner, text= "Age", font="Tahoma 15")
    age_spinbox = tk.Spinbox(formdesigner, from_=5, to=100, font="Tahoma 15")
    age.grid(row=2, column=0)
    age_spinbox.grid(row=3, column=0)

    nationality = tk.Label(formdesigner, text="Nationality", font="Tahoma 15")
    nationality_combobox = ttk.Combobox(formdesigner, values=["America", "Myanmar", "China", "Africa", "Thailand", "India"], font="Tahoma 15")
    nationality.grid(row=2, column=1)
    nationality_combobox.grid(row=3, column=1)
    
    title = tk.Label(formdesigner, text= "Title", font="Tahoma 15")
    title_combobox = ttk.Combobox(formdesigner, values=["Mr.", "Ms."], font="Tahoma 15")
    title.grid(row=2, column=2)
    title_combobox.grid(row=3, column=2)
    
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
            
    firstname = tk.Label(window, text= "First name", font="Tahoma 15")
    firstname.grid(row=0, column=0, padx=10,pady=10)
    lastname = tk.Label(window, text="Last name", font="Tahoma 15")
    lastname.grid(row=0, column=1, padx=10,pady=10)
    nickname = tk.Label(window, text = "Nick name", font="Tahoma 15")
    nickname.grid(row=0, column=2, padx=10,pady=10)
    firstname = tk.Entry(window, font="Tahoma 15")
    lastname = tk.Entry(window, font="Tahoma 15")
    nickname = tk.Entry(window, font="Tahoma 15")

    firstname.grid(row=1, column=0, padx=10,pady=10)
    lastname.grid(row=1, column=1, padx=10,pady=10)
    nickname.grid(row=1, column=2, padx=10,pady=10)

    age = tk.Label(window, text= "Age", font="Tahoma 15")
    age_spinbox = tk.Spinbox(window, from_=5, to=100, font="Tahoma 15")
    age.grid(row=2, column=0)
    age_spinbox.grid(row=3, column=0)
    nationality = tk.Label(window, text="Nationality", font="Tahoma 15")
    nationality_combobox = ttk.Combobox(window, values=["America", "Myanmar", "China", "Africa", "Thailand", "India"], font="Tahoma 15")
    nationality.grid(row=2, column=1)
    nationality_combobox.grid(row=3, column=1)

    title = tk.Label(window, text= "Title", font="Tahoma 15")
    title_combobox = ttk.Combobox(window, values=["Mr.", "Ms."], font="Tahoma 15")
    title.grid(row=2, column=2)
    title_combobox.grid(row=3, column=2)

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