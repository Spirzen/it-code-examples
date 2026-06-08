// Обязательное значение
String name = config.getValue("app.name", String.class);

// Опциональное значение
Optional<Integer> port = config.getOptionalValue("app.port", Integer.class);

// Со значениями по умолчанию
int timeout = config.getValue("app.timeout", int.class, () -> 30);

// Списки
List<Integer> ports = config.getValues("app.ports", Integer.class);

// Map (ключ=значение, по строковому шаблону)
Map<String, String> props = config.getValues("app.datasource", String.class, String.class);
// → app.datasource.url, app.datasource.username → {url=..., username=...}
