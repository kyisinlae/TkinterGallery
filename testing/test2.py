import tkinter as tk
from tkinter import *

window = tk.Tk()
labeltitle=tk.Label(text="Welcome!", bg="white",fg="blue", font="Consolas 11")
labeltitle.pack(side="top", fill="both", anchor="w")    
label1=tk.Label(text="This is a label.", bg="white",fg="black", font="Consolas 11")
label1.pack(side="top", fill="both", anchor="w")
label2=tk.Label(text="We can change the font style.", bg="white",fg="black", font=("arial italic", 11) )
label2.pack(side="top", fill="both", anchor="w")
label3=tk.Label(text="This is a disable label.", bg="white", fg="black", font="Consolas 11", state='disabled')
label3.pack(side="top", fill="both", anchor="w")
label4=tk.Label(text="This is a normal label.", bg="white", fg="black", font="Consolas 11")
label4.pack(side="top", fill="both", anchor="w")
label5=tk.Label(text="We can also change the font color.", bg="white", fg="red", font="Consolas 11")
label5.pack(side="top", fill="both", anchor="w")

Label(window, text="Flat border", borderwidth=3, relief="flat", padx=5, pady=10).pack(padx=5, pady=10)
Label(window, text="raised border", borderwidth=3, relief="raised", padx=5, pady=10).pack(padx=5, pady=10)
Label(window, text="sunken border", borderwidth=3, relief="sunken", padx=5, pady=10).pack(padx=5, pady=10)
Label(window, text="ridge border", borderwidth=3, relief="ridge", padx=5, pady=10).pack(padx=5, pady=10)
Label(window, text="solid border", borderwidth=3, relief="solid", padx=5, pady=10).pack(padx=5, pady=10)
Label(window, text="groove border", borderwidth=3, relief="groove",padx=5, pady=10).pack(padx=5, pady=10)

window.mainloop()