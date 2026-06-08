
import 'dart:convert';
import 'dart:io';

Future<void> saveConfig(Map<String, Object?> config) async {
  final json = jsonEncode(config);
  await File('config.json').writeAsString(json);
}

Future<Map<String, dynamic>> loadConfig() async {
  final file = File('config.json');
  if (!await file.exists()) return {};
  final raw = await file.readAsString();
  return jsonDecode(raw) as Map<String, dynamic>;
}
