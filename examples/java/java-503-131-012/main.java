
import java.util.Comparator;
import java.util.stream.Stream;

public class ProcessViewer {
    public static void main(String[] args) {
        System.out.println("Список запущенных процессов:");
        System.out.println("PID\t\tName");
        System.out.println("---------------------------");

        // Stream API для обработки процесса
        try (Stream<ProcessHandle> processes = ProcessHandle.allProcesses()) {
            processes
                .sorted(Comparator.comparingLong(ProcessHandle::pid))
                .forEach(process -> {
                    long pid = process.pid();
                    String name = process.info().command().orElse("N/A");
                    
                    // Ограничение вывода первых 100 символов имени
                    if (name.length() > 100) {
                        name = name.substring(0, 97) + "...";
                    }
                    
                    System.out.printf("%d\t%s%n", pid, name);
                });
        }
    }
}
