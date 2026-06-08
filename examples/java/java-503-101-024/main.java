public class ReportGenerator {
    private volatile ReportTemplate template;
    
    private ReportTemplate getTemplate() {
        ReportTemplate result = template;
        if (result == null) {
            synchronized (this) {
                result = template;
                if (result == null) {
                    template = result = loadTemplate();
                }
            }
        }
        return result;
    }
    
    private ReportTemplate loadTemplate() {
        // Загрузка шаблона из файла или базы данных
        return templateRepository.loadDefault();
    }
}
