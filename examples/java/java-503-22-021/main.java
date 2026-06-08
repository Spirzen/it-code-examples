
import org.springframework.stereotype.Service;
import reactor.core.publisher.Mono;

@Service
public class ReactiveBookService {

    private final ReactiveBookRepository bookRepository;

    public ReactiveBookService(ReactiveBookRepository bookRepository) {
        this.bookRepository = bookRepository;
    }

    public Mono<Book> createBook(String title, String author, String isbn, Integer year) {
        Book book = new Book(title, author, isbn, year);
        return bookRepository.save(book);
    }

    public Mono<Book> getBook(Long id) {
        return bookRepository.findById(id);
    }

    public Flux<Book> getAvailableBooks() {
        return bookRepository.findByAvailable(true);
    }

    public Flux<ReactiveBookRepository.BookPreview> getRecentPreviews() {
        return bookRepository.findRecentPreviews();
    }

    public Mono<Void> markAsUnavailable(Long id) {
        return bookRepository.findById(id)
            .flatMap(book -> {
                Book updated = new Book(
                    book.id(),
                    book.title(),
                    book.author(),
                    book.isbn(),
                    book.publishedYear(),
                    false
                );
                return bookRepository.save(updated).then();
            });
    }
}
