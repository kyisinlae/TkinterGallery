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