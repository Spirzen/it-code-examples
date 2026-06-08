// Абстракция: контракт
public interface Logger {
    void log(LogLevel level, String message);
}

// Абстрактный класс: частичная реализация + инкапсуляция
public abstract class BufferedLogger implements Logger {
    private final Queue<String> buffer = new LinkedList<>();
    private final int bufferSize;

    protected BufferedLogger(int bufferSize) {
        this.bufferSize = bufferSize;
    }

    @Override
    public final void log(LogLevel level, String message) {
        String entry = format(level, message);
        buffer.add(entry);
        if (buffer.size() >= bufferSize) {
            flush();
        }
    }

    protected abstract String format(LogLevel level, String message);
    protected abstract void writeBatch(List<String> batch);

    private void flush() {
        List<String> batch = new ArrayList<>(buffer);
        buffer.clear();
        writeBatch(batch); // делегирование — инкапсуляция внутреннего буфера сохраняется
    }
}

// Конкретная реализация — полиморфизм в действии
public class FileLogger extends BufferedLogger {
    private final PrintWriter writer;

    public FileLogger(int bufferSize, PrintWriter writer) {
        super(bufferSize);
        this.writer = writer;
    }

    @Override protected String format(LogLevel level, String message) {
        return Instant.now() + " [" + level + "] " + message;
    }

    @Override protected void writeBatch(List<String> batch) {
        batch.forEach(writer::println);
        writer.flush();
    }
}
