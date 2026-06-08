import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(home: const SettingsScreen());
  }
}

class SettingsScreen extends StatefulWidget {
  const SettingsScreen({super.key});

  @override
  State<SettingsScreen> createState() => _SettingsScreenState();
}

class _SettingsScreenState extends State<SettingsScreen> {
  bool _notify = true;
  bool _sound = false;
  String _role = 'user';

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Настройки')),
      body: ListView(
        padding: const EdgeInsets.all(16),
        children: [
          SwitchListTile(
            title: const Text('Уведомления'),
            subtitle: const Text('Push о новых сообщениях'),
            value: _notify,
            onChanged: (v) => setState(() => _notify = v),
          ),
          SwitchListTile(
            title: const Text('Звук'),
            value: _sound,
            onChanged: (v) => setState(() => _sound = v),
          ),
          const Divider
          const Text('Роль', style: TextStyle(fontWeight: FontWeight.bold)),
          RadioListTile<String>(
            title: const Text('Пользователь'),
            value: 'user',
            groupValue: _role,
            onChanged: (v) => setState(() => _role = v!),
          ),
          RadioListTile<String>(
            title: const Text('Администратор'),
            value: 'admin',
            groupValue: _role,
            onChanged: (v) => setState(() => _role = v!),
          ),
          const SizedBox(height: 16),
          Text(
            'Итог: роль «$_role»; уведомления: $_notify; звук: $_sound',
            style: TextStyle(color: Colors.grey.shade700),
          ),
        ],
      ),
    );
  }
}
