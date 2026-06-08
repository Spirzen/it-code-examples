
import org.springframework.Data.r2dbc.repository.Query;
import org.springframework.Data.r2dbc.repository.R2dbcRepository;
import org.springframework.Data.repository.reactive.ReactiveSortingRepository;
import reactor.core.publisher.Flux;
import reactor.core.publisher.Mono;

public interface ReactiveBookRepository extends R2dbcRepository<Book, Long> {

    Flux<Book> findByAvailable(boolean available);

    Mono<Book> findByIsbn(String isbn);

    // Проекция через record
    record BookPreview(String title, String author) {}

    @Query("SELECT title, author FROM books WHERE available = true ORDER BY published_year DESC LIMIT 5")
    Flux<BookPreview> findRecentPreviews();
}
