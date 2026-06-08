// Текущий момент в UTC
Instant now = Instant.now();

// Преобразование в московское время
ZonedDateTime moscowTime = now.atZone(ZoneId.of("Europe/Moscow"));

// Дата события в локальном формате (без привязки к поясу)
LocalDateTime eventTime = LocalDateTime.of(2025, 11, 18, 15, 0);

// Перевод события в часовой пояс клиента
ZonedDateTime clientTime = eventTime.atZone(ZoneId.of("Asia/Yekaterinburg"));

// Форматирование для пользователя
DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd MMMM yyyy, HH:mm", Locale.forLanguageTag("ru"));
String display = clientTime.format(formatter); // "18 ноября 2025, 17:00"
