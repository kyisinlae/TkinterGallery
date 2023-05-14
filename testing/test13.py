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