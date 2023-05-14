import tkinter as tk
from tkinter import ttk
from tkinter import *
import pyperclip as pc
from tkinter import messagebox

def openMessageBox(root):
    
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
    formlable = tk.Label(formtitle,text="Tab", font="Tahoma 15", height=1, bg="white", pady=5)
    formlable.pack(side="top", anchor="center")
    formdesigner = tk.Frame(formView, background="white", padx=10,pady=10)
    formdesigner.pack(side="top", fill="both", expand=True)
    
    panedwindow.add(formView, weight=5)  
    panedwindow.add(codeView, weight=2)
    
    def clickMessageAlert():
        messagebox.showinfo("showinfo", "Information")
        messagebox.showwarning("showwarning", "Warning")
        messagebox.showerror("showerror", "Error")
    
    def clickMessageQuestoin():
        result = messagebox.askquestion("askquestion", "Are you sure?")
        if (result == True):
            messagebox.showinfo("result", "Yes")
        else:
            messagebox.showinfo("result", "No")

    def clickMessageOKCancel():
        result = messagebox.askokcancel("askokcancel", "Want to continue?")
        if (result == True):
            messagebox.showinfo("result", "OK")
        else:
            messagebox.showinfo("result", "Cancel")
            
    def clickMessageYesNo():
        result = messagebox.askyesno("askyesno", "Find the value?")
        if (result == True):
            messagebox.showinfo("result", "Yes")
        else:
            messagebox.showinfo("result", "No")
            
    def clickMessageRetryCancel():
        result = messagebox.askretrycancel("askretrycancel", "Try again?")
        if (result == True):
            messagebox.showinfo("result", "Retry")
        else:
            messagebox.showinfo("result", "Cancel")
        
    def clickMessageYesNoCancel():
        result = messagebox.askyesnocancel("askyesnocancel", "Try again?")
        if (result == True):
            messagebox.showinfo("result", "Yes")
        elif (result == False):
            messagebox.showinfo("result", "No")
        else:
            messagebox.showinfo("result", "Cancel")
            
        
    buttonAlert = Button(formdesigner, text="Show Alert message", command=clickMessageAlert)
    buttonQuestion = Button(formdesigner, text="Question message", command=clickMessageQuestoin)
    buttonOKCancel = Button(formdesigner, text="Show Ok / Cancel message", command=clickMessageOKCancel)
    buttonYesNo = Button(formdesigner, text="Show Yes / No message", command=clickMessageYesNo)
    buttonRetryCancel = Button(formdesigner, text="Show Retry message", command=clickMessageRetryCancel)
    buttonYesNoCancel = Button(formdesigner, text="Show Yes / No / Cancel message", command=clickMessageYesNoCancel)


    buttonAlert.pack()
    buttonOKCancel.pack()
    buttonYesNo.pack()
    buttonRetryCancel.pack()
    buttonYesNoCancel.pack()
    
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
    
    
    from tkinter import *
    from tkinter import messagebox
        
    root = Tk()
    root.geometry("300x200")


    def clickMessageAlert():
        messagebox.showinfo("showinfo", "Information")
        messagebox.showwarning("showwarning", "Warning")
        messagebox.showerror("showerror", "Error")
        
    def clickMessageQuestoin():
        result = messagebox.askquestion("askquestion", "Are you sure?")
        if (result == True):
            messagebox.showinfo("result", "Yes")
        else:
            messagebox.showinfo("result", "No")

    def clickMessageOKCancel():
        result = messagebox.askokcancel("askokcancel", "Want to continue?")
        if (result == True):
            messagebox.showinfo("result", "OK")
        else:
            messagebox.showinfo("result", "Cancel")
            
    def clickMessageYesNo():
        result = messagebox.askyesno("askyesno", "Find the value?")
        if (result == True):
            messagebox.showinfo("result", "Yes")
        else:
            messagebox.showinfo("result", "No")
            
    def clickMessageRetryCancel():
        result = messagebox.askretrycancel("askretrycancel", "Try again?")
        if (result == True):
            messagebox.showinfo("result", "Retry")
        else:
            messagebox.showinfo("result", "Cancel")
        
    def clickMessageYesNoCancel():
        result = messagebox.askyesnocancel("askyesnocancel", "Try again?")
        if (result == True):
            messagebox.showinfo("result", "Yes")
        elif (result == False):
            messagebox.showinfo("result", "No")
        else:
            messagebox.showinfo("result", "Cancel")
            
        
    buttonAlert = Button(root, text="Show Alert message", command=clickMessageAlert)
    buttonQuestion = Button(root, text="Question message", command=clickMessageQuestoin)
    buttonOKCancel = Button(root, text="Show Ok / Cancel message", command=clickMessageOKCancel)
    buttonYesNo = Button(root, text="Show Yes / No message", command=clickMessageYesNo)
    buttonRetryCancel = Button(root, text="Show Retry message", command=clickMessageRetryCancel)
    buttonYesNoCancel = Button(root, text="Show Yes / No / Cancel message", command=clickMessageYesNoCancel)


    buttonAlert.pack()
    buttonOKCancel.pack()
    buttonYesNo.pack()
    buttonRetryCancel.pack()
    buttonYesNoCancel.pack()

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