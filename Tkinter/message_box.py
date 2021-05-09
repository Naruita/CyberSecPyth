from tkinter import *
import tkinter.messagebox

root = Tk()
tkinter.messagebox.showinfo("Title", "We've only just begun.")

resp = tkinter.messagebox.askquestion("Question 1", "Do you wish to continue?")
if resp == 'yes':
    tkinter.messagebox.showinfo("Title", 'Here is the continuation.')
else:
    tkinter.messagebox.showinfo('Title', 'Well, fine then.')

root.mainloop()