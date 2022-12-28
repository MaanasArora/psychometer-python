from dataclasses import dataclass

from core.models.likert import LikertResult, LikertTest


@dataclass
class LikertSession:
    test: LikertTest

    def __post_init__(self):
        self.answers = [None for _ in self.test.questions]

    def set_answer(self, question_index: int, answer: int):
        self.answers[question_index] = answer

    def score(self):
        return LikertResult.from_answers(self.test, self.answers)