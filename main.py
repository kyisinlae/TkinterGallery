from tkinter import Tk, Menu
from tkinter import *
import frame_layout
import components.label as label
import about
import splash
import components.entry as entry
import components.checkbox as checkbox
import components.switch as switch
import components.button as button
import components.radiobutton as radiobutton
import components.combobox as combobox
import components.scale as scale
import components.scrollbar as scrollbar
import components.spinbox as spinbox

def clickAbout():
    about.openAbout(root)
def clickFrameLayout():
    frame_layout.openFrameLayout(root)
def clickLabel():
    label.openLableForm(root)
def clickEntryForm():
    entry.openEntryForm(root)
def clickCheckBox():
    checkbox.opencheckbox(root)
def clickSwitch():
    switch.openSwitch(root)
def clickButton():
    button.openButton(root)
def clickRadioButton():
    radiobutton.openRadioButton(root)
def clickCombobox():
    combobox.openCombobox(root)
def clickScale():
    scale.openScale(root)
def clickScrollBar():
    scrollbar.openScrollBar(root)
def clickSpinBox():
    spinbox.openSpinBox(root)


root = Tk()
root.title('Tkinter Gallery Project')
menubar = Menu(root)
root.config(menu=menubar)

root.config(bg = 'grey')
file_menu = Menu(
    menubar,
    tearoff=0
)

file_menu.add_command(label='Frame Layout', command=clickFrameLayout)

sub_menu = Menu(file_menu, tearoff=0)
sub_menu.add_command(label='Label', command=clickLabel)
sub_menu.add_command(label='Entry', command=clickEntryForm)
sub_menu.add_command(label='Checkbox', command=clickCheckBox)
sub_menu.add_command(label='Switch', command=clickSwitch) #//
sub_menu.add_command(label='Button', command=clickButton)
sub_menu.add_command(label='Radio Button', command=clickRadioButton)#//
sub_menu.add_command(label='Combobox', command=clickCombobox)
sub_menu.add_command(label='Scale',command=clickScale)
sub_menu.add_command(label='Scrollbar', command=clickScrollBar)
sub_menu.add_command(label='Spinbox', command=clickSpinBox)
sub_menu.add_command(label='Progress bar')
sub_menu.add_command(label='Tab')
sub_menu.add_command(label='Treeview')
sub_menu.add_command(label='Message box')
sub_menu.add_command(label='Dialog box')
sub_menu.add_command(label='Color picker')

# add the File menu to the menubar
file_menu.add_cascade(
    label="Components",
    menu=sub_menu
)

# add Exit menu item
file_menu.add_separator()

file_menu.add_command(
    label='Exit',
    command=root.destroy
)

menubar.add_cascade(
    label="Menu",
    menu=file_menu,
    underline=0
)




# create the Help menu
help_menu = Menu(
    menubar,
    tearoff=0
)
help_menu.add_command(label='About...', command=clickAbout)

# add the Help menu to the menubar
menubar.add_cascade(
    label="Help",
    menu=help_menu,
    underline=0
)

root.withdraw()
splash.show_splash(root)

# root.geometry('800x600')
# root.deiconify()

root.state("zoomed")
root.mainloop()