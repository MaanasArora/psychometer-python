class LikertResultScore {
  const LikertResultScore(this.score, this.value);

  final LikertScore score;
  final double value;

  double deviation() {
    return (value - score.mean!) / score.stdev!;
  }
}

class LikertResult {
  const LikertResult(this.scores);

  final List<LikertResultScore> scores;
}

class LikertScore {
  const LikertScore(
      this.name, this.questionIndices, this.weights, this.mean, this.stdev);

  final String name;
  final Set<int> questionIndices;
  final Map<int, double> weights;

  final double? mean;
  final double? stdev;

  double getMaxScore() {
    double maxPositive = 5 *
        weights.values.where((value) => value > 0).reduce(
              (value, element) => value + element,
            );
    double minNegative = 1 *
        weights.values
            .where((value) => value < 0)
            .reduce((value, element) => value + element);

    return maxPositive + minNegative;
  }

  double getMinScore() {
    double minPositive = 1 *
        weights.values.where((value) => value > 0).reduce(
              (value, element) => value + element,
            );
    double maxNegative = 5 *
        weights.values
            .where((value) => value < 0)
            .reduce((value, element) => value + element);

    return minPositive + maxNegative;
  }

  double evaluate(List<int> responses) {
    double value = 0;

    for (int index in questionIndices) {
      value += weights[index]! * responses[index];
    }

    return value;
  }
}

class LikertTest {
  const LikertTest(this.name, this.questions, this.scores);

  final String name;
  final List<String> questions;
  final List<LikertScore> scores;

  LikertResult score(List<int> responses) {
    List<LikertResultScore> resultScores = [];

    for (LikertScore score in scores) {
      double value = score.evaluate(responses);

      resultScores.add(LikertResultScore(score, value));
    }

    return LikertResult(resultScores);
  }
}
