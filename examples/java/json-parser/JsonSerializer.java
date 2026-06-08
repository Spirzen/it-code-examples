import java.math.BigDecimal;
import java.util.List;
import java.util.Map;

final class JsonSerializer {
    private final StringBuilder sb = new StringBuilder();

    public String serialize(JsonValue value) {
        appendValue(value);
        return sb.toString();
    }

    private void appendValue(JsonValue value) {
        switch (value) {
            case JsonString s -> appendString(s.value());
            case JsonNumber n -> appendNumber(n.value());
            case JsonBoolean b -> sb.append(b.value());
            case JsonNull _ -> sb.append("null");
            case JsonArray a -> appendArray(a.elements());
            case JsonObject o -> appendObject(o.fields());
        }
    }

    private void appendString(String s) {
        sb.append('"');
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            switch (c) {
                case '"'  -> sb.append("\\\"");
                case '\\' -> sb.append("\\\\");
                case '\b' -> sb.append("\\b");
                case '\f' -> sb.append("\\f");
                case '\n' -> sb.append("\\n");
                case '\r' -> sb.append("\\r");
                case '\t' -> sb.append("\\t");
                default -> {
                    if (c < 0x20 || c > 0x7E) {
                        sb.append(String.format("\\u%04x", (int) c));
                    } else {
                        sb.append(c);
                    }
                }
            }
        }
        sb.append('"');
    }

    private void appendNumber(BigDecimal n) {
        sb.append(n.toPlainString());
    }

    private void appendArray(List<JsonValue> elements) {
        sb.append('[');
        for (int i = 0; i < elements.size(); i++) {
            if (i > 0) sb.append(',');
            appendValue(elements.get(i));
        }
        sb.append(']');
    }

    private void appendObject(Map<String, JsonValue> fields) {
        sb.append('{');
        int i = 0;
        for (Map.Entry<String, JsonValue> entry : fields.entrySet()) {
            if (i++ > 0) sb.append(',');
            appendString(entry.getKey());
            sb.append(':');
            appendValue(entry.getValue());
        }
        sb.append('}');
    }
}
