
import java.util.Map;
import java.util.Optional;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.atomic.AtomicLong;
import org.springframework.stereotype.Service;

@Service
public class NoteService {
    private final Map<Long, String> store = new ConcurrentHashMap<>();
    private final AtomicLong seq = new AtomicLong();

    public record Note(long id, String text) {}

    public Note create(String text) {
        long id = seq.incrementAndGet();
        store.put(id, text);
        return new Note(id, text);
    }

    public Optional<Note> find(long id) {
        return Optional.ofNullable(store.get(id)).map(t -> new Note(id, t));
    }
}
