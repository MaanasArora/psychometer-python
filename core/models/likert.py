from dataclasses import dataclass


@dataclass
class LikertQuestion:
    question: str


@dataclass
class LikertScoreQuestion:
    question_number: int
    weight: float


@dataclass
class LikertScore:
    name: str
    description: str
    questions: list[LikertScoreQuestion]

    def score(self, answers: list[int]):
        return sum(
            [
                answers[q.question_number] * q.weight
                for q in self.questions
            ]
        )


@dataclass
class LikertTest:
    name: str
    description: str
    questions: list[LikertQuestion]
    scoring: list[LikertScore]


@dataclass
class LikertResult:
    test: LikertTest
    scores: list[float]

    @staticmethod
    def from_answers(test: LikertTest, answers: list[int]):
        scores = [scoring.score(answers) for scoring in test.scoring]

        return LikertResult(test, scores)
