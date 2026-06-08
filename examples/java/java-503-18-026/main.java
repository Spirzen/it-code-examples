public sealed interface Expr
    permits Literal, BinaryOp, FunctionCall {}

final class Literal implements Expr {
    private final int value;
    public Literal(int value) { this.value = value; }
    public int value() { return value; }
}

non-sealed class BinaryOp implements Expr {
    private final String op;
    private final Expr left, right;
    // ...
}

// FunctionCall — final или non-sealed, но обязан быть упомянут в permits
