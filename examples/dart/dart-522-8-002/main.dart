sealed class Result<T> {}

final class Ok<T> extends Result<T> {
  final T value;
  Ok(this.value);
}

final class Err<T> extends Result<T> {
  final String message;
  Err(this.message);
}

String explain(Result<int> r) => switch (r) {
  Ok(value: var v) => 'успех: $v',
  Err(message: var m) => 'ошибка: $m',
};
