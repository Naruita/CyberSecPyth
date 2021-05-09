from tkinter import *
from time import sleep

def test_function():
    print("Gonna do it for real next time.")

def save_function():
    print("Saved.")
    sleep(2)
    print("I lied.")

def print_undo():
    print("You cannot undo your sins, George.")

def simple_test():
    print("You've run the command.")

root = Tk()

drop_menu = Menu(root)
root.config(menu=drop_menu)

sub_menu = Menu(drop_menu)

drop_menu.add_cascade(label="File", menu=sub_menu)

sub_menu.add_command(label="Project", command=test_function)
sub_menu.add_command(label="Save", command=save_function)
sub_menu.add_separator()
sub_menu.add_command(label="Exit", command=exit)

sub_menu_2 = Menu(drop_menu)

drop_menu.add_cascade(label="Edit", menu=sub_menu_2)
sub_menu_2.add_command(label="Undo", command=print_undo)

toolbar = Frame(root, bg="pink")
insert_button = Button(toolbar, text="Insert File", command=simple_test)
insert_button.pack(side=LEFT, padx=2, pady=3)

print_button = Button(toolbar, text="print", command=simple_test)
print_button.pack(side=LEFT, padx=2, pady=3)

toolbar.pack(side=TOP, fill=X)

status_bar = Label(root, text="Status Bar", bd=1, relief=SUNKEN, anchor=W)
status_bar.pack(side=BOTTOM, padx=2, fill=X)

root.mainloop()