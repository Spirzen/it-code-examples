import java.time.LocalDateTime;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.HashMap;
import java.util.Map;

record ConfigMemento(Map<String, String> properties, LocalDateTime timestamp) {
    ConfigMemento {
        properties = Map.copyOf(properties);
    }
}

class ServerConfig {
    private final Map<String, String> properties = new HashMap<>();

    void set(String key, String value) {
        properties.put(key, value);
    }

    String get(String key) {
        return properties.get(key);
    }

    ConfigMemento save() {
        return new ConfigMemento(properties, LocalDateTime.now());
    }

    void restore(ConfigMemento memento) {
        properties.clear();
        properties.putAll(memento.properties());
    }
}

class ConfigHistory {
    private final Deque<ConfigMemento> snapshots = new ArrayDeque<>();

    void backup(ServerConfig config) {
        snapshots.push(config.save());
    }

    void undo(ServerConfig config) {
        if (!snapshots.isEmpty()) {
            config.restore(snapshots.pop());
        }
    }
}
