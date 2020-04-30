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

root.mainloop()