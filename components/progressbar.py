import tkinter as tk
from tkinter import ttk
from tkinter import *
import pyperclip as pc
from tkinter.messagebox import showinfo

def openProgressBar(formdesigner):
    
    for widget in formdesigner.winfo_children():
        if isinstance(widget, ttk.PanedWindow):
            widget.destroy()

    panedwindow=ttk.Panedwindow(formdesigner, orient=HORIZONTAL)
    panedwindow.pack(fill=BOTH, expand=True)
    # formView=ttk.Frame(panedwindow,width=100,height=300, relief=SUNKEN)  
    # codeView=ttk.Frame(panedwindow,width=400,height=400, relief=SUNKEN)
    formView=ttk.Frame(panedwindow, relief=SUNKEN)  
    codeView=ttk.Frame(panedwindow, width=100,relief=SUNKEN)
    formtitle=tk.Frame(formView, background="white")
    formtitle.pack(side="top", fill="x", anchor="center")
    formlable = tk.Label(formtitle,text="Progress Bar", font="Tahoma 15", height=1, bg="white", pady=5)
    formlable.pack(side="top", anchor="center")
    formdesigner = tk.Frame(formView, background="white", padx=10,pady=10)
    formdesigner.pack(side="top", fill="both", expand=True)
    
    panedwindow.add(formView, weight=5)  
    panedwindow.add(codeView, weight=2)
    
    def update_progress_label():
        return f"Current Progress: {pb['value']}%"


    def progress():
        if pb['value'] < 100:
            pb['value'] += 20
            value_label['text'] = update_progress_label()
        else:
            showinfo(message='The progress completed!')


    def stop():
        pb.stop()
        value_label['text'] = update_progress_label()


    # progressbar
    pb = ttk.Progressbar(
        formdesigner,
        orient='horizontal',
        mode='determinate',
        length=280
    )
    # place the progressbar
    pb.grid(row=0, column=0, columnspan=2, padx=10, pady=20)

    # label
    value_label = ttk.Label(formdesigner, text=update_progress_label())
    value_label.grid(row=1, column=0, columnspan=2)

    # start button
    start_button = ttk.Button(
        formdesigner,
        text='Progress',
        command=progress
    )
    start_button.grid(row=2, column=0, padx=10, pady=10, sticky=tk.E)

    stop_button = ttk.Button(
        formdesigner,
        text='Stop',
        command=stop
    )
    stop_button.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)
    #///

    # progressbar
    pb1 = ttk.Progressbar(
        formdesigner,
        orient='horizontal',
        mode='indeterminate',
        length=280
    )
    # place the progressbar
    pb1.grid(row=0, column=3, columnspan=2, padx=10, pady=20)


    # start button
    start_button1 = ttk.Button(
        formdesigner,
        text='Start',
        command=pb1.start
    )
    start_button1.grid(row=1, column=3, padx=10, pady=10, sticky=tk.E)

    # stop button
    stop_button1 = ttk.Button(
        formdesigner,
        text='Stop',
        command=pb1.stop
    )
    stop_button1.grid(row=1, column=4, padx=10, pady=10, sticky=tk.W)
    #///

    pb2 = ttk.Progressbar(
        formdesigner,
        orient='horizontal',
        mode='determinate',
        length=280
    )
    # place the progressbar
    pb2.grid(row=0, column=6, columnspan=2, padx=10, pady=20)

    # start button
    start_button2 = ttk.Button(
        formdesigner,
        text='Start',
        command=pb2.start
    )
    start_button2.grid(row=1, column=6, padx=10, pady=10, sticky=tk.E)

    # stop button
    stop_button2 = ttk.Button(
        formdesigner,
        text='Stop',
        command=pb2.stop
    )
    stop_button2.grid(row=1, column=7, padx=10, pady=10, sticky=tk.W)
    
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
    
    
    from tkinter import ttk
    import tkinter as tk
    from tkinter.messagebox import showinfo


    # root window
    root = tk.Tk()
    root.geometry('300x120')
    root.title('Progressbar Demo')

    def update_progress_label():
        return f"Current Progress: {pb['value']}%"


    def progress():
        if pb['value'] < 100:
            pb['value'] += 20
            value_label['text'] = update_progress_label()
        else:
            showinfo(message='The progress completed!')


    def stop():
        pb.stop()
        value_label['text'] = update_progress_label()


    # progressbar
    pb = ttk.Progressbar(
        root,
        orient='horizontal',
        mode='determinate',
        length=280
    )
    # place the progressbar
    pb.grid(row=0, column=0, columnspan=2, padx=10, pady=20)

    # label
    value_label = ttk.Label(root, text=update_progress_label())
    value_label.grid(row=1, column=0, columnspan=2)

    # start button
    start_button = ttk.Button(
        root,
        text='Progress',
        command=progress
    )
    start_button.grid(row=2, column=0, padx=10, pady=10, sticky=tk.E)

    stop_button = ttk.Button(
        root,
        text='Stop',
        command=stop
    )
    stop_button.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)
    #///

    # progressbar
    pb1 = ttk.Progressbar(
        root,
        orient='horizontal',
        mode='indeterminate',
        length=280
    )
    # place the progressbar
    pb1.grid(row=0, column=3, columnspan=2, padx=10, pady=20)


    # start button
    start_button1 = ttk.Button(
        root,
        text='Start',
        command=pb1.start
    )
    start_button1.grid(row=1, column=3, padx=10, pady=10, sticky=tk.E)

    # stop button
    stop_button1 = ttk.Button(
        root,
        text='Stop',
        command=pb1.stop
    )
    stop_button1.grid(row=1, column=4, padx=10, pady=10, sticky=tk.W)
    #///

    pb2 = ttk.Progressbar(
        root,
        orient='horizontal',
        mode='determinate',
        length=280
    )
    # place the progressbar
    pb2.grid(row=0, column=6, columnspan=2, padx=10, pady=20)

    # start button
    start_button2 = ttk.Button(
        root,
        text='Start',
        command=pb2.start
    )
    start_button2.grid(row=1, column=6, padx=10, pady=10, sticky=tk.E)

    # stop button
    stop_button2 = ttk.Button(
        root,
        text='Stop',
        command=pb2.stop
    )
    stop_button2.grid(row=1, column=7, padx=10, pady=10, sticky=tk.W)

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