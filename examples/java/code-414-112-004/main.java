// Антипаттерн: создание объекта в цикле
public String buildReport(List<Record> records) {
    String result = "";
    for (Record record : records) {
        result = result + record.toString() + "\n"; // Создаёт новый String каждый раз
    }
    return result;
}

// Правильный паттерн: использование StringBuilder
public String buildReport(List<Record> records) {
    StringBuilder builder = new StringBuilder(records.size() * 64);
    for (Record record : records) {
        builder.append(record.toString()).append('\n');
    }
    return builder.toString();
}
