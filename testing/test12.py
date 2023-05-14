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