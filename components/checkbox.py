import tkinter as tk
from tkinter import ttk
from tkinter import *
import pyperclip as pc
from tkinter.messagebox import showinfo

def opencheckbox(root):
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
    
    formtitle=tk.Frame(formView, background="white")
    formtitle.pack(side="top", fill="x", anchor="center")
    formlable = tk.Label(formtitle,text="Checkbox", font="Tahoma20", height=1, bg="white", pady=5)
    formlable.pack(side="top", anchor="center")
    formdesigner = tk.Frame(formView, background="white", padx=10,pady=10)
    formdesigner.pack(side="top", fill="both", expand=True)
    panedwindow.add(formView, weight=5)  
    panedwindow.add(codeView, weight=2)
    
    
    
    
    frame1 = tk.Frame(formdesigner, background="gray", padx=10,pady=10)
    
    resultString = tk.StringVar()
    def checkbox_changed():
        tk.messagebox.showinfo(title='Result',message=resultString.get())
        if(resultString.get() =='Ok, Bye!!') :
            checkYes.config(state=DISABLED)
            checkNo.config(state=DISABLED)
        else:
            checkYes.config(state=NORMAL)
            checkNo.config(state=NORMAL)
            
    checkQuestion = Checkbutton(frame1, font="Tahoma 15", anchor="w",
                    text='Do you know python language?',
                    command=checkbox_changed,
                    variable=resultString,
                    onvalue='Yes, That''s great',
                    offvalue='Ok, Bye!!')
    
    checkQuestion.select()
    checkQuestion.pack()
    
    Label(frame1, text ='Is Python similar to Java or C++?', font="Tahoma 15").pack(side=TOP, anchor=W)
    Checkbutton(frame1, text ='Nothing', font="Tahoma 15", takefocus=0, state="disabled").pack(side=TOP, anchor=W)
    
    checkYes = tk.Checkbutton(frame1, text ='Java', font="Tahoma 15", takefocus = 0)
    checkNo = Checkbutton(frame1, text ='C++', font="Tahoma 15", takefocus = 0)
    checkYes.pack(side=TOP, anchor=W)
    checkNo.pack(side=TOP, anchor=W)
    
    frame1.place(in_=formdesigner, anchor="c", relx=.5, rely=.5)

    
    
    
    
    
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

    window = Tk()

    Label(window, text ='Foods to choose.', font="Tahoma 15").place(x = 20, y = 10)
    
    pizza = Checkbutton(window, text ='Pizza', font="Tahoma 15",
                    takefocus = 0).place(x = 40, y = 40)

    apple = Checkbutton(window, text ='Apple', font="Tahoma 15",
                    takefocus = 0).place(x = 40, y = 90)

    chocolate = Checkbutton(window, text ='Chocolate', font="Tahoma 15",
                    takefocus = 0).place(x = 40, y = 140)

    cookie = Checkbutton(window, text ='Cookie', font="Tahoma 15",
                    takefocus = 0).place(x = 40, y = 190)

    Label(window, text='Drinks to choose.', font="Tahoma 15").place(x = 260, y=10)

    lemonade = Checkbutton(window, text='Lemonade', font="Tahoma 15",
                    takefocus= 0).place(x=280, y=40)

    applejuice = Checkbutton(window, text='Apple Juice', font="Tahoma 15",
                    takefocus = 0).place(x=280, y=90)

    bubbletea = Checkbutton(window, text='Bubble Tea', font="Tahoma 15",
                    takefocus = 0).place(x=280, y=140)

    milk = Checkbutton(window, text='Milk', font="Tahoma 15",
                    takefocus = 0).place(x=280, y=190)

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
    