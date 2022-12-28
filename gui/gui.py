from tkinter import *
from tkinter.ttk import *

from core.models.likert import LikertQuestion, LikertScore, LikertScoreQuestion, LikertTest

from gui.tests.likert import LikertTestWindow


class Gui:
    def __init__(self):
        self.build_root()
        self.build_welcome()
        self.build_start_sample()

    def build_root(self):
        self.root = Tk()
        self.root.title("Psychometer")
        self.root.resizable(False, False)

    def build_welcome(self):
        self.welcome = Label(self.root, text="Welcome to Psychometer")
        self.welcome.pack()

    def build_start_sample(self):
        self.start = Button(
            self.root, text="Start Sample Test", command=self.start_sample_test)
        self.start.pack()

    def start_sample_test(self):
        sample_test = LikertTest("Sample Test", "This is a sample test", [
            LikertQuestion("This is a sample question"),
            LikertQuestion("This is another sample question"),
            LikertQuestion("This is yet another sample question"),
        ], [
            LikertScore("Sample Score", "This is a sample score", [
                LikertScoreQuestion(0, 1),
                LikertScoreQuestion(1, 1),
                LikertScoreQuestion(2, 1),
            ]),
        ])
        
        self.start_test(sample_test)

    def start_test(self, test: LikertTest):
        self.test = LikertTestWindow(self.root, test)

    def run(self):
        self.root.mainloop()
