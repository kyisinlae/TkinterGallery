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
