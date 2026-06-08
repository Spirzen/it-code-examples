import java.math.BigDecimal;
import java.util.List;
import java.util.Map;
import java.util.Objects;

sealed interface JsonValue permits
    JsonString, JsonNumber, JsonBoolean, JsonNull, JsonArray, JsonObject {

    default String asString() {
        if (this instanceof JsonString s) return s.value();
        throw new JsonTypeException("Expected string, got " + getClass().getSimpleName());
    }

    default BigDecimal asNumber() {
        if (this instanceof JsonNumber n) return n.value();
        throw new JsonTypeException("Expected number, got " + getClass().getSimpleName());
    }

    default boolean asBoolean() {
        if (this instanceof JsonBoolean b) return b.value();
        throw new JsonTypeException("Expected boolean, got " + getClass().getSimpleName());
    }

    default List<JsonValue> asArray() {
        if (this instanceof JsonArray a) return a.elements();
        throw new JsonTypeException("Expected array, got " + getClass().getSimpleName());
    }

    default Map<String, JsonValue> asObject() {
        if (this instanceof JsonObject o) return o.fields();
        throw new JsonTypeException("Expected object, got " + getClass().getSimpleName());
    }

    default boolean isNull() {
        return this instanceof JsonNull;
    }
}

final class JsonTypeException extends RuntimeException {
    JsonTypeException(String message) { super(message); }
}

record JsonString(String value) implements JsonValue {
    JsonString { Objects.requireNonNull(value, "value must not be null"); }
}

record JsonNumber(BigDecimal value) implements JsonValue {
    JsonNumber { Objects.requireNonNull(value, "value must not be null"); }
}

record JsonBoolean(boolean value) implements JsonValue { }

final class JsonNull implements JsonValue {
    private static final JsonNull INSTANCE = new JsonNull();
    private JsonNull() { }
    public static JsonNull getInstance() { return INSTANCE; }
    @Override public String toString() { return "null"; }
}

record JsonArray(List<JsonValue> elements) implements JsonValue {
    JsonArray { Objects.requireNonNull(elements, "elements must not be null"); }
}

record JsonObject(Map<String, JsonValue> fields) implements JsonValue {
    JsonObject { Objects.requireNonNull(fields, "fields must not be null"); }
}
