from tkinter import *
from time import sleep
import webbrowser as webb

class my_buttons:
    def __init__(self, rootone):
        frame = Frame(rootone)
        frame.pack()

        self.printButton = Button(frame, text="Click Here for VENOM", command=self.spew_venom)
        self.printButton.pack()
        self.exitButton = Button(frame, text="Exit", command=frame.quit)
        self.exitButton.pack()

    def spew_venom(self):
        print("Eminem.")
        sleep(3)
        print("VENOM")
        webb.open("https://youtu.be/8CdcCD5V-d8")


if __name__ == "__main__":
    root = Tk()
    b = my_buttons(root)
    root.mainloop()
