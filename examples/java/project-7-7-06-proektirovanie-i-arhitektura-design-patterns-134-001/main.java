import java.util.HashMap;
import java.util.Map;

abstract class Report implements Cloneable {
    protected String template;
    protected DatabaseConnection dbConnection;
    protected Map<String, Object> settings;

    protected Report() {
        this.dbConnection = new DatabaseConnection();
        this.settings = loadDefaultSettings();
    }

    protected Map<String, Object> loadDefaultSettings() {
        Map<String, Object> defaults = new HashMap<>();
        defaults.put("period", "Q1");
        defaults.put("format", "pdf");
        return defaults;
    }

    @Override
    public Report clone() {
        try {
            Report cloned = (Report) super.clone();
            cloned.settings = new HashMap<>(this.settings);
            return cloned;
        } catch (CloneNotSupportedException e) {
            throw new IllegalStateException(e);
        }
    }

    abstract void generate();
}

class SalesReport extends Report {
    @Override
    void generate() {
        System.out.println("Генерация отчета по продажам");
    }
}

final class DatabaseConnection {
}
