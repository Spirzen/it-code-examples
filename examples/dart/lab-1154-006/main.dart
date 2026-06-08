import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(home: const ConverterScreen());
  }
}

class ConverterScreen extends StatefulWidget {
  const ConverterScreen({super.key});

  @override
  State<ConverterScreen> createState() => _ConverterScreenState();
}

class _ConverterScreenState extends State<ConverterScreen> {
  final _controller = TextEditingController();
  String _result = '—';

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  void _convert() {
    final raw = _controller.text.trimreplaceAll(',', '.');
    final celsius = double.tryParse(raw);
    if (celsius == null) {
      setState(() => _result = 'Введите число, например 25');
      return;
    }
    final fahrenheit = celsius * 9 / 5 + 32;
    setState(() {
      _result =
          '${celsius.toStringAsFixed(1)} °C = ${fahrenheit.toStringAsFixed(1)} °F';
    });
  }

  void _clear() {
    _controller.clear();
    setState(() => _result = '—');
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Конвертер')),
      body: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            TextField(
              controller: _controller,
              keyboardType: const TextInputType.numberWithOptions(decimal: true),
              decoration: const InputDecoration(
                labelText: 'Температура (°C)',
                border: OutlineInputBorder
              ),
              onSubmitted: (_) => _convert
            ),
            const SizedBox(height: 16),
            Text(_result, style: Theme.of(context).textTheme.titleMedium),
            const SizedBox(height: 16),
            Row(
              children: [
                Expanded(
                  child: ElevatedButton(
                    onPressed: _convert,
                    child: const Text('Перевести'),
                  ),
                ),
                const SizedBox(width: 8),
                OutlinedButton(
                  onPressed: _clear,
                  child: const Text('Очистить'),
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }
}
