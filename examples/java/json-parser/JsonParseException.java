final class JsonParseException extends RuntimeException {
    private final int position;
    private final int line;
    private final int column;

    JsonParseException(String message, int position, int line, int column) {
        super(String.format("%s at line %d, column %d (position %d)", message, line, column, position));
        this.position = position;
        this.line = line;
        this.column = column;
    }

    public int getPosition() { return position; }
    public int getLine() { return line; }
    public int getColumn() { return column; }
}
