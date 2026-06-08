// Плохо: создание множества промежуточных объектов String
public String buildReport(List<Order> orders) {
    String result = "";
    for (Order order : orders) {
        result += order.getId() + ": " + order.getTotal() + "\n";
    }
    return result;
}

// Хорошо: эффективная конкатенация
public String buildReport(List<Order> orders) {
    StringBuilder sb = new StringBuilder();
    for (Order order : orders) {
        sb.append(order.getId())
          .append(": ")
          .append(order.getTotal())
          .append("\n");
    }
    return sb.toString();
}
