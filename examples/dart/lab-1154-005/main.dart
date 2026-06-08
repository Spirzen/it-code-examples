import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(home: const GreetingScreen());
  }
}

class GreetingScreen extends StatefulWidget {
  const GreetingScreen({super.key});

  @override
  State<GreetingScreen> createState() => _GreetingScreenState();
}

class _GreetingScreenState extends State<GreetingScreen> {
  final _controller = TextEditingController();
  String _message = '—';

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  void _greet() {
    final name = _controller.text.trim();
    setState(() {
      _message = name.isEmpty ? 'Введите имя' : 'Здравствуй, $name!';
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Приветствие')),
      body: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            TextField(
              controller: _controller,
              decoration: const InputDecoration(
                labelText: 'Ваше имя',
                border: OutlineInputBorder
                hintText: 'Анна',
              ),
              textInputAction: TextInputAction.done,
              onSubmitted: (_) => _greet
            ),
            const SizedBox(height: 12),
            Text(_message, style: const TextStyle(fontSize: 16)),
            const SizedBox(height: 12),
            ElevatedButton(
              onPressed: _greet,
              child: const Text('Приветствовать'),
            ),
          ],
        ),
      ),
    );
  }
}
