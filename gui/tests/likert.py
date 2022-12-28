from typing import Callable
from dataclasses import dataclass

from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox as mb

from core.models.likert import LikertQuestion, LikertResult, LikertTest
from core.sessions.likert import LikertSession


@dataclass
class LikertQuestionWidget:
    master: Frame
    question: LikertQuestion
    set_response: Callable[[int], None]

    def __post_init__(self):
        self.response = IntVar()

        self.build_question()
        self.build_responses()

    def lift_response(self):
        self.set_response(self.response.get())

    def build_question(self):
        self.question = Label(self.master, text=self.question.question)
        self.question.pack(anchor=W, pady=10)

    def build_responses(self):
        self.responses = Frame(self.master)
        self.responses.pack(anchor=W, padx=20)

        response_texts = [
            'Strongly Agree', 'Agree', 'Neutral', 'Disagree', 'Strongly Disagree'
        ]
        for i, response_text in enumerate(response_texts, 1):
            Radiobutton(self.responses, text=response_text, variable=self.response,
                        command=self.lift_response, value=i).pack(anchor=W)


@dataclass
class LikertResultWindow:
    master: Tk
    result: LikertResult

    def __post_init__(self):
        self.build_root()
        self.build_title()
        self.build_scores()

    def build_root(self):
        self.root = Toplevel()
        self.root.title(f"Psychometer - Result: {self.result.test.name}")
        self.root.resizable(False, False)

    def build_title(self):
        Label(self.root, text=self.result.test.name, underline=1).pack()

    def build_scores(self):
        for scoring, score in zip(self.result.test.scoring, self.result.scores):
            Label(self.root, text=f"{scoring.name}: {score:.2f}").pack(anchor=W, padx=20)


@dataclass
class LikertTestWindow:
    master: Tk
    test: LikertTest

    def __post_init__(self):
        self.session = LikertSession(self.test)

        self.build_root()
        self.build_title()
        self.build_questions()
        self.build_score()

    def set_response_callable(self, index):
        def set_response(response):
            self.session.answers[index] = response

        return set_response

    def build_root(self):
        self.root = Toplevel()
        self.root.title(f"Psychometer - Running Test: {self.test.name}")
        self.root.resizable(False, False)

    def build_title(self):
        self.title = Label(self.root, text=self.test.name, underline=1)
        self.title.pack()

    def build_questions(self):
        for i, question in enumerate(self.test.questions):
            LikertQuestionWidget(self.root, question,
                                 self.set_response_callable(i))

    def show_result(self):
        if all(self.session.answers):
            LikertResultWindow(self.master, self.session.score())
            self.root.destroy()
        else:
            mb.showerror('Error', 'Please answer all questions')

    def build_score(self):
        self.score = Button(self.root, text="Show results",
                            command=self.show_result)
        self.score.pack()
