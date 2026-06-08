import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(home: const SliderScreen());
  }
}

class SliderScreen extends StatefulWidget {
  const SliderScreen({super.key});

  @override
  State<SliderScreen> createState() => _SliderScreenState();
}

class _SliderScreenState extends State<SliderScreen> {
  double _volume = 50;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Громкость')),
      body: Padding(
        padding: const EdgeInsets.all(24),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text(
              'Уровень: ${_volume.round()}',
              style: const TextStyle(fontSize: 22),
            ),
            Slider(
              min: 0,
              max: 100,
              divisions: 20,
              label: _volume.roundtoString
              value: _volume,
              onChanged: (v) => setState(() => _volume = v),
            ),
          ],
        ),
      ),
    );
  }
}
