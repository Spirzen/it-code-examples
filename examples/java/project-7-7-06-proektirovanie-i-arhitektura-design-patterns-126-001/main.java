import java.util.ArrayDeque;
import java.util.Deque;

interface Command {
    void execute();
    void undo();
}

class TextEditor {
    private final StringBuilder text = new StringBuilder();

    void insert(int pos, String str) {
        text.insert(pos, str);
    }

    void delete(int pos, int length) {
        text.delete(pos, pos + length);
    }

    String getText() {
        return text.toString();
    }
}

class InsertCommand implements Command {
    private final TextEditor editor;
    private final int position;
    private final String text;

    InsertCommand(TextEditor editor, int position, String text) {
        this.editor = editor;
        this.position = position;
        this.text = text;
    }

    @Override
    public void execute() {
        editor.insert(position, text);
    }

    @Override
    public void undo() {
        editor.delete(position, text.length());
    }
}

class CommandHistory {
    private final Deque<Command> history = new ArrayDeque<>();

    void execute(Command cmd) {
        cmd.execute();
        history.push(cmd);
    }

    void undo() {
        if (!history.isEmpty()) {
            history.pop().undo();
        }
    }
}
