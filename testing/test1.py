import tkinter as tk

root = tk.Tk()
root.geometry("600x400")

toolbar = tk.Frame(root, background="yellow", height=40)
statusbar = tk.Frame(root, background="red", height=20)
main = tk.Frame(root, background="green", height=20)


toolbar.pack(side="top", fill="x")
statusbar.pack(side="bottom", fill="x")
main.pack(side="top", fill="both", expand=True)

left_pane = tk.Frame(main, background="pink", width=100)
right_pane = tk.Frame(main, background="cyan", width=200)

left_pane.pack(side="left", fill="y")
right_pane.pack(side="right", fill="y")

custom_pane = tk.Frame(main, background="orange", height=200, width=200)
custom_pane.pack(side="bottom", anchor="se") # // n, ne, e, se, s, sw, w, nw, or center

root.mainloop()