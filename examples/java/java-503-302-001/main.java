
import java.util.ArrayList;
import java.util.List;

public class LeakDemo {
    static final List<byte[]> LEAK = new ArrayList<>();

    public static void main(String[] args) throws InterruptedException {
        while (true) {
            LEAK.add(new byte[1024 * 1024]); // 1 MiB
            Thread.sleep(100);
        }
    }
}
