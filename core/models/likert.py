from dataclasses import dataclass


@dataclass
class LikertQuestion:
    question: str


@dataclass
class LikertScoreQuestion:
    question: LikertQuestion
    weight: float


@dataclass
class LikertScore:
    name: str
    description: str
    questions: list[LikertScoreQuestion]

    def score(self, answers: list[int]):
        return sum(
            [
                answers[i] * q.weight
                for i, q in enumerate(self.questions)
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

    def from_answers(self, test: LikertTest, answers: list[int]):
        scores = map(LikertScore.score, test.scoring, answers)

        return LikertResult(test, scores)
