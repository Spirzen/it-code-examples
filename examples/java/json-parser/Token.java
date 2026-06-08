import java.math.BigDecimal;

sealed interface Token permits
    LeftBrace, RightBrace, LeftBracket, RightBracket,
    Colon, Comma, StringToken, NumberToken,
    TrueToken, FalseToken, NullToken, EndOfInput { }

record LeftBrace(int position) implements Token { }
record RightBrace(int position) implements Token { }
record LeftBracket(int position) implements Token { }
record RightBracket(int position) implements Token { }
record Colon(int position) implements Token { }
record Comma(int position) implements Token { }
record StringToken(String value, int position) implements Token { }
record NumberToken(BigDecimal value, String raw, int position) implements Token { }
record TrueToken(int position) implements Token { }
record FalseToken(int position) implements Token { }
record NullToken(int position) implements Token { }
record EndOfInput(int position) implements Token { }
