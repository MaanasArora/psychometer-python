import 'package:flutter/material.dart';
import 'package:psychometer/likert/model.dart';
import 'package:psychometer/likert/result.dart';
import 'package:psychometer/likert/test.dart';
import 'package:psychometer/test_model/test.dart';

void main() {
  runApp(const Application());
}

class Application extends StatefulWidget {
  const Application({super.key});

  @override
  State<Application> createState() => _ApplicationState();
}

class _ApplicationState extends State<Application> {
  LikertTest? thisTest;

  @override
  void initState() {
    super.initState();
    LikertTestSerializer.fromResource("tests/sample-test.json").then((value) {
      setState(() {
        thisTest = value;
      });
    });
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
        title: 'Psychometer',
        theme: ThemeData(
          primarySwatch: Colors.green,
          fontFamily: 'Nunito',
        ),
        routes: {
          '/': (context) => thisTest != null
              ? HomeScreen(testName: thisTest!.name)
              : const LoadingScreen(),
          '/test': (context) => LikertTestScreen(
              questions: thisTest!.questions,
              onSubmit: (List<int> responses) => {
                    Navigator.of(context).pushNamed("/result",
                        arguments: thisTest!.score(responses))
                  }),
          '/result': (context) => const ResultsScreen()
        });
  }
}

class LoadingScreen extends StatelessWidget {
  const LoadingScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        body: Padding(
            padding: const EdgeInsets.all(40),
            child: Column(
              children: const [CircularProgressIndicator()],
            )));
  }
}

class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key, required this.testName});

  final String testName;

  void startTest(context) {
    Navigator.of(context).pushNamed("/test");
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        body: Padding(
            padding: const EdgeInsets.all(30),
            child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  const Text("Welcome to Psychometer",
                      style: TextStyle(fontSize: 30)),
                  const SizedBox(height: 15),
                  Text(testName),
                  const SizedBox(height: 30),
                  ElevatedButton(
                      onPressed: () {
                        startTest(context);
                      },
                      child: const Text("Start Test"))
                ])));
  }
}
