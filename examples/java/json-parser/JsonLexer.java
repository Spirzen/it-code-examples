import java.math.BigDecimal;
import java.util.Objects;

final class JsonLexer {
    private final String input;
    private int index = 0;
    private int line = 1;
    private int column = 1;
    private Token bufferedToken = null;

    JsonLexer(String input) {
        this.input = Objects.requireNonNull(input, "input must not be null");
    }

    public Token nextToken() {
        if (bufferedToken != null) {
            Token t = bufferedToken;
            bufferedToken = null;
            return t;
        }

        skipWhitespace();

        if (index >= input.length()) {
            return new EndOfInput(position());
        }

        char c = input.charAt(index);
        int startPos = position();

        switch (c) {
            case '{' -> { index++; return new LeftBrace(startPos); }
            case '}' -> { index++; return new RightBrace(startPos); }
            case '[' -> { index++; return new LeftBracket(startPos); }
            case ']' -> { index++; return new RightBracket(startPos); }
            case ':' -> { index++; return new Colon(startPos); }
            case ',' -> { index++; return new Comma(startPos); }
            case '"' -> return parseString(startPos);
            case '-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' -> return parseNumber(startPos);
            case 't' -> return parseKeyword("true", new TrueToken(startPos), startPos);
            case 'f' -> return parseKeyword("false", new FalseToken(startPos), startPos);
            case 'n' -> return parseKeyword("null", new NullToken(startPos), startPos);
            default -> throw error("Unexpected character: '" + c + "'");
        }
    }

    public Token peek() {
        if (bufferedToken == null) {
            bufferedToken = nextToken();
        }
        return bufferedToken;
    }

    public void putBack(Token token) {
        if (bufferedToken != null) {
            throw new IllegalStateException("Buffer already full");
        }
        bufferedToken = token;
    }

    public int getLine() { return line; }
    public int getColumn() { return column; }

    private void skipWhitespace() {
        while (index < input.length()) {
            char c = input.charAt(index);
            if (c == ' ' || c == '\t' || c == '\n' || c == '\r') {
                advance();
            } else {
                break;
            }
        }
    }

    private Token parseString(int startPos) {
        advance();
        StringBuilder sb = new StringBuilder();
        while (index < input.length()) {
            char c = input.charAt(index);
            if (c == '"') {
                advance();
                return new StringToken(sb.toString(), startPos);
            }
            if (c == '\\') {
                advance();
                if (index >= input.length()) {
                    throw error("Unterminated escape sequence in string");
                }
                c = input.charAt(index);
                switch (c) {
                    case '"'  -> { sb.append('"');  advance(); }
                    case '\\' -> { sb.append('\\'); advance(); }
                    case '/'  -> { sb.append('/');  advance(); }
                    case 'b'  -> { sb.append('\b'); advance(); }
                    case 'f'  -> { sb.append('\f'); advance(); }
                    case 'n'  -> { sb.append('\n'); advance(); }
                    case 'r'  -> { sb.append('\r'); advance(); }
                    case 't'  -> { sb.append('\t'); advance(); }
                    case 'u'  -> {
                        advance();
                        if (index + 4 > input.length()) {
                            throw error("Incomplete \\u escape: expected 4 hex digits");
                        }
                        String hex = input.substring(index, index + 4);
                        try {
                            int codePoint = Integer.parseInt(hex, 16);
                            sb.appendCodePoint(codePoint);
                            index += 4;
                            column += 4;
                        } catch (NumberFormatException e) {
                            throw error("Invalid hex digits in \\u escape: '" + hex + "'");
                        }
                    }
                    default -> throw error("Invalid escape sequence: \\" + c);
                }
            } else {
                sb.append(c);
                advance();
            }
        }
        throw error("Unterminated string");
    }

    private Token parseNumber(int startPos) {
        int start = index;

        if (peekChar() == '-') {
            advance();
        }

        if (peekChar() == '0') {
            advance();
            char next = peekChar();
            if (next >= '0' && next <= '9') {
                throw error("Invalid number: leading zero");
            }
        } else if (isDigit(peekChar())) {
            do { advance(); } while (isDigit(peekChar()));
        } else {
            throw error("Invalid number: missing digits after sign");
        }

        if (peekChar() == '.') {
            advance();
            if (!isDigit(peekChar())) {
                throw error("Invalid number: missing digits after '.'");
            }
            do { advance(); } while (isDigit(peekChar()));
        }

        char c = peekChar();
        if (c == 'e' || c == 'E') {
            advance();
            c = peekChar();
            if (c == '+' || c == '-') {
                advance();
            }
            if (!isDigit(peekChar())) {
                throw error("Invalid number: missing digits after exponent indicator");
            }
            do { advance(); } while (isDigit(peekChar()));
        }

        String raw = input.substring(start, index);
        try {
            BigDecimal value = new BigDecimal(raw);
            return new NumberToken(value, raw, startPos);
        } catch (NumberFormatException e) {
            throw error("Invalid number format: '" + raw + "'");
        }
    }

    private Token parseKeyword(String keyword, Token token, int startPos) {
        if (index + keyword.length() > input.length()) {
            throw error("Unexpected end of input while parsing '" + keyword + "'");
        }
        String candidate = input.substring(index, index + keyword.length());
        if (!candidate.equals(keyword)) {
            throw error("Expected '" + keyword + "', got '" + candidate + "'");
        }
        index += keyword.length();
        column += keyword.length();
        return token;
    }

    private char peekChar() {
        return index < input.length() ? input.charAt(index) : '\0';
    }

    private boolean isDigit(char c) {
        return c >= '0' && c <= '9';
    }

    private void advance() {
        if (index >= input.length()) return;
        char c = input.charAt(index);
        if (c == '\n') {
            line++;
            column = 1;
        } else if (c == '\r') {
            if (index + 1 < input.length() && input.charAt(index + 1) == '\n') {
                index++;
            }
            line++;
            column = 1;
        } else {
            column++;
        }
        index++;
    }

    private int position() {
        return index;
    }

    private JsonParseException error(String message) {
        return new JsonParseException(message, position(), line, column);
    }
}
