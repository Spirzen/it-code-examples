import java.util.HashMap;
import java.util.Map;

interface DataService {
    String getData(String key);
}

class DatabaseService implements DataService {
    @Override
    public String getData(String key) {
        return "data_from_db_" + key;
    }
}

abstract class DataServiceDecorator implements DataService {
    protected final DataService delegate;

    protected DataServiceDecorator(DataService delegate) {
        this.delegate = delegate;
    }
}

class LoggingDecorator extends DataServiceDecorator {
    LoggingDecorator(DataService delegate) {
        super(delegate);
    }

    @Override
    public String getData(String key) {
        System.out.println("LOG: запрос " + key);
        String result = delegate.getData(key);
        System.out.println("LOG: ответ получен");
        return result;
    }
}

class CachingDecorator extends DataServiceDecorator {
    private final Map<String, String> cache = new HashMap<>();

    CachingDecorator(DataService delegate) {
        super(delegate);
    }

    @Override
    public String getData(String key) {
        return cache.computeIfAbsent(key, delegate::getData);
    }
}
