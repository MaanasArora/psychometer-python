from tkinter import *


class Gui:
    def __init__(self):
        self.build_root()
        self.build_welcome()

    def build_root(self):
        self.root = Tk()
        self.root.title("Psychometer")
        self.root.geometry("800x600")
        self.root.resizable(False, False)

    def build_welcome(self):
        self.welcome = Label(self.root, text="Welcome to Psychometer")
        self.welcome.pack()

    def run(self):
        self.root.mainloop()