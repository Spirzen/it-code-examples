
import java.lang.Thread;
import java.util.Map;

Map<Thread, StackTraceElement[]> stacks = Thread.getAllStackTraces();
for (Map.Entry<Thread, StackTraceElement[]> entry : stacks.entrySet()) {
    System.out.println("Поток: " + entry.getKey().getName());
    for (StackTraceElement element : entry.getValue()) {
        System.out.println("  " + element);
    }
}
