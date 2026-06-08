import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Objects;

final class JsonParser {
    private final JsonLexer lexer;
    private Token currentToken;

    JsonParser(JsonLexer lexer) {
        this.lexer = Objects.requireNonNull(lexer, "lexer must not be null");
        this.currentToken = lexer.nextToken();
    }

    public JsonValue parse() {
        JsonValue result = parseValue();
        if (!(lexer.peek() instanceof EndOfInput)) {
            throw error("Unexpected token after top-level value");
        }
        return result;
    }

    private JsonValue parseValue() {
        return switch (currentToken) {
            case LeftBrace _     -> parseObject();
            case LeftBracket _   -> parseArray();
            case StringToken t   -> { consume(); yield new JsonString(t.value()); }
            case NumberToken t   -> { consume(); yield new JsonNumber(t.value()); }
            case TrueToken _     -> { consume(); yield new JsonBoolean(true); }
            case FalseToken _    -> { consume(); yield new JsonBoolean(false); }
            case NullToken _     -> { consume(); yield JsonNull.getInstance(); }
            default -> throw error("Expected value");
        };
    }

    private JsonObject parseObject() {
        consume();
        Map<String, JsonValue> map = new LinkedHashMap<>();

        if (currentToken instanceof RightBrace) {
            consume();
            return new JsonObject(map);
        }

        while (true) {
            if (!(currentToken instanceof StringToken keyToken)) {
                throw error("Expected string (key)");
            }
            String key = keyToken.value();
            consume();

            if (!(currentToken instanceof Colon)) {
                throw error("Expected ':' after key");
            }
            consume();

            JsonValue value = parseValue();
            map.put(key, value);

            if (currentToken instanceof Comma) {
                consume();
                if (currentToken instanceof RightBrace) {
                    throw error("Trailing comma in object");
                }
            } else if (currentToken instanceof RightBrace) {
                consume();
                break;
            } else {
                throw error("Expected ',' or '}' after value");
            }
        }

        return new JsonObject(map);
    }

    private JsonArray parseArray() {
        consume();
        List<JsonValue> list = new ArrayList<>();

        if (currentToken instanceof RightBracket) {
            consume();
            return new JsonArray(list);
        }

        while (true) {
            list.add(parseValue());

            if (currentToken instanceof Comma) {
                consume();
                if (currentToken instanceof RightBracket) {
                    throw error("Trailing comma in array");
                }
            } else if (currentToken instanceof RightBracket) {
                consume();
                break;
            } else {
                throw error("Expected ',' or ']' after value");
            }
        }

        return new JsonArray(list);
    }

    private void consume() {
        currentToken = lexer.nextToken();
    }

    private JsonParseException error(String message) {
        int pos = currentToken instanceof EndOfInput
            ? lexer.getColumn()
            : tokenPosition(currentToken);
        return new JsonParseException(
            message + ", got " + tokenName(currentToken),
            pos, lexer.getLine(), lexer.getColumn()
        );
    }

    private int tokenPosition(Token t) {
        return switch (t) {
            case LeftBrace b -> b.position();
            case RightBrace b -> b.position();
            case LeftBracket b -> b.position();
            case RightBracket b -> b.position();
            case Colon c -> c.position();
            case Comma c -> c.position();
            case StringToken s -> s.position();
            case NumberToken n -> n.position();
            case TrueToken tok -> tok.position();
            case FalseToken tok -> tok.position();
            case NullToken tok -> tok.position();
            case EndOfInput e -> e.position();
        };
    }

    private String tokenName(Token t) {
        return switch (t) {
            case LeftBrace _ -> "'{'";
            case RightBrace _ -> "'}'";
            case LeftBracket _ -> "'['";
            case RightBracket _ -> "']'";
            case Colon _ -> "':'";
            case Comma _ -> "','";
            case StringToken s -> "string \"" + s.value() + "\"";
            case NumberToken n -> "number " + n.raw();
            case TrueToken _ -> "'true'";
            case FalseToken _ -> "'false'";
            case NullToken _ -> "'null'";
            case EndOfInput _ -> "end of input";
        };
    }
}
