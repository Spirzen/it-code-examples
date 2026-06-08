import java.io.IOException;
import java.io.Reader;
import java.util.Objects;

public final class Json {

    private Json() { }

    public static JsonValue parse(String json) {
        Objects.requireNonNull(json, "json must not be null");
        return new JsonParser(new JsonLexer(json)).parse();
    }

    public static String stringify(JsonValue value) {
        Objects.requireNonNull(value, "value must not be null");
        return new JsonSerializer().serialize(value);
    }

    public static JsonValue parse(Reader reader) throws IOException {
        StringBuilder sb = new StringBuilder();
        char[] buf = new char[8192];
        int n;
        while ((n = reader.read(buf)) != -1) {
            sb.append(buf, 0, n);
        }
        return parse(sb.toString());
    }
}
