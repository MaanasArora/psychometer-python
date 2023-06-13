import 'package:flutter/material.dart';
import 'package:psychometer/likert/model.dart';

class ResultsScreen extends StatelessWidget {
  const ResultsScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final result = ModalRoute.of(context)!.settings.arguments as LikertResult;

    return Scaffold(
        body: Padding(
            padding: const EdgeInsets.all(30),
            child: Column(
              mainAxisAlignment: MainAxisAlignment.start,
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                const Text(
                  "Results",
                  style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
                ),
                const SizedBox(height: 30),
                ...result.scores
                    .map((score) => [
                          Text("${score.score.name}: ${score.value}"),
                          const SizedBox(height: 10)
                        ])
                    .expand((element) => element)
              ],
            )));
  }
}
