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