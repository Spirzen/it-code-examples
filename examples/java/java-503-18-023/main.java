abstract class ReportGenerator {
    protected String title;

    public ReportGenerator(String title) {
        this.title = title;
    }

    // общая реализация — неизменяемая часть алгоритма
    public final String generate() {
        StringBuilder sb = new StringBuilder();
        sb.append("=== ").append(title).append(" ===\n");
        sb.append(generateHeader()).append("\n");
        sb.append(generateBody()).append("\n");
        sb.append(generateFooter());
        return sb.toString();
    }

    // абстрактные методы — вариативная часть, реализуется в подклассах
    protected abstract String generateHeader();
    protected abstract String generateBody();
    protected abstract String generateFooter();
}

class SalesReport extends ReportGenerator {
    public SalesReport() { super("Отчёт по продажам"); }

    @Override protected String generateHeader() { return "Период: Q3 2025"; }
    @Override protected String generateBody()   { return "Итого: 1 250 000 ₽"; }
    @Override protected String generateFooter() { return "Подпись: главбух"; }
}
