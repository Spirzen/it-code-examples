
import 'dart:convert';
import 'dart:io';

class Task {
  final int id;
  final String title;
  bool done;
  Task({required this.id, required this.title, this.done = false});
  Map<String, dynamic> toJson() => {'id': id, 'title': title, 'done': done};
  factory Task.fromJson(Map<String, dynamic> j) =>
      Task(id: j['id'], title: j['title'], done: j['done'] ?? false);
}

Future<List<Task>> load(String path) async {
  if (!await File(path).exists()) return [];
  final list = jsonDecode(await File(path).readAsString()) as List;
  return list.map((e) => Task.fromJson(e as Map<String, dynamic>)).toList();
}
