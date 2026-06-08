import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(home: const ButtonDemo());
  }
}

class ButtonDemo extends StatelessWidget {
  const ButtonDemo({super.key});

  void _showMessage(BuildContext context) {
    ScaffoldMessenger.of(context).showSnackBar(
      const SnackBar(
        content: Text('Кнопка нажата!'),
        duration: Duration(seconds: 2),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Кнопка')),
      body: Center(
        child: ElevatedButton(
          onPressed: () => _showMessage(context),
          child: const Text('Нажми меня'),
        ),
      ),
    );
  }
}
