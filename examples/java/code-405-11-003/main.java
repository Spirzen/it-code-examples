
import java.lang.Thread;

Thread[] threads = new Thread[100];
int count = Thread.enumerate(threads);
for (int i = 0; i < count; i++) {
    System.out.println(threads[i].getName());
}
