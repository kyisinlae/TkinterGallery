import tkinter as tk
from tkinter import *
from tkinter.messagebox import showinfo

window = Tk()

frame1 = tk.Frame(window, background="gray", padx=10,pady=10)

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
                onvalue='Yes, That''s great!',
                offvalue='Ok, Bye!!')

checkQuestion.select()
checkQuestion.pack()

Label(frame1, text ='Is Python similar to Java or C++?', font="Tahoma 15").pack(side=TOP, anchor=W)
Checkbutton(frame1, text ='Nothing', font="Tahoma 15", takefocus=0, state="disabled").pack(side=TOP, anchor=W)

checkYes = tk.Checkbutton(frame1, text ='Java', font="Tahoma 15", takefocus = 0)
checkNo = Checkbutton(frame1, text ='C++', font="Tahoma 15", takefocus = 0)
checkYes.pack(side=TOP, anchor=W)
checkNo.pack(side=TOP, anchor=W)

frame1.place(in_=window, anchor="c", relx=.5, rely=.5)

window.mainloop()