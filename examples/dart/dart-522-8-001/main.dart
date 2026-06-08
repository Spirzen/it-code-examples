(String, int) parseId(String raw) {
  final parts = raw.split(':');
  return (parts[0], int.parse(parts[1]));
}

String format((String, int) pair) => switch (pair) {
  ('', _) => 'пустой ключ',
  (var name, var age) when age < 0 => 'некорректный возраст для $name',
  (var name, var age) => '$name — $age лет',
};

void demo() {
  final named = (name: 'Анна', score: 90);
  final msg = switch (named) {
    (name: 'Анна', score: >= 85) => 'отлично, $name',
    (name: var n, score: var s) => '$n: $s баллов',
  };
  print(msg);
}
