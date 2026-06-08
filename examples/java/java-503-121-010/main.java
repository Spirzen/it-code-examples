public class DatabaseConfigSource implements ConfigSource {
    private final Map<String, String> properties = loadFromDatabase();

    @Override
    public int getOrdinal() {
        return 500; // выше System props
    }

    @Override
    public Set<String> getPropertyNames() {
        return properties.keySet();
    }

    @Override
    public String getValue(String propertyName) {
        return properties.get(propertyName);
    }

    @Override
    public String getName() {
        return "DatabaseConfigSource";
    }
}
