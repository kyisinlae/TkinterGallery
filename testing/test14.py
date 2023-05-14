import os
import tkinter as tk
from tkinter import ttk

root=tk.Tk()
root.geometry('320x240')

frame1 = tk.Frame(root)
tk.Label(frame1, text='Directory Tree View').pack()
directoryTreeView=ttk.Treeview(frame1,show='tree')
scorll_h1=tk.Scrollbar(frame1,orient=tk.VERTICAL,command=directoryTreeView.yview)
directoryTreeView.configure(yscroll=scorll_h1.set)
directory='./'
directoryTreeView.heading('#0',text='Dir:'+directory,anchor='w')
path=os.path.abspath(directory)
node=directoryTreeView.insert('','end',text=path,open=True)
def traverse_dir(parent,path):
    for d in os.listdir(path):
        full_path=os.path.join(path,d)
        isdir = os.path.isdir(full_path)
        id=directoryTreeView.insert(parent,'end',text=d,open=False)
        if isdir:
            traverse_dir(id,full_path)
traverse_dir(node,path)
scorll_h1.pack(side=tk.RIGHT,fill=tk.Y)
directoryTreeView.pack()
frame1.pack()



frame2 = tk.Frame(root)
tk.Label(frame2, text='Data Tree View').pack()

treeView = ttk.Treeview(frame2,show='tree')
scorll_h2=tk.Scrollbar(frame2,orient=tk.VERTICAL,command=treeView.yview)
treeView.configure(yscroll=scorll_h2.set)

treeView.heading('#0', text='Departments', anchor=tk.W)


# adding data
treeView.insert('', tk.END, text='Programming Language', iid=0, open=False)
treeView.insert('', tk.END, text='Python', iid=1, open=False)
treeView.insert('', tk.END, text='C++', iid=2, open=False)
treeView.insert('', tk.END, text='Java', iid=3, open=False)
treeView.insert('', tk.END, text='Dart', iid=4, open=False)

treeView.insert('', tk.END, text='VB.NET', iid=5, open=False)
treeView.insert('', tk.END, text='C#', iid=6, open=False)
treeView.insert('', tk.END, text='Java Script', iid=7, open=False)
treeView.insert('', tk.END, text='C', iid=8, open=False)
treeView.insert('', tk.END, text='F#', iid=9, open=False)
treeView.insert('', tk.END, text='Ruby', iid=10, open=False)
treeView.insert('', tk.END, text='Go', iid=11, open=False)
treeView.insert('', tk.END, text='HTML', iid=12, open=False)
treeView.insert('', tk.END, text='CSS', iid=13, open=False)
treeView.insert('', tk.END, text='Tkinter', iid=14, open=False)

treeView.move(5, 0, 0)
treeView.move(6, 0, 1)
treeView.move(7, 0, 2)
treeView.move(1, 0, 3)
treeView.move(14, 1, 0)
scorll_h2.pack(side=tk.RIGHT,fill=tk.Y)
treeView.pack()
frame2.pack()
root.mainloop()