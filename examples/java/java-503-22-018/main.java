
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;
import java.util.Optional;

@Service
@Transactional
public class BookService {

    private final BookRepository bookRepository;

    public BookService(BookRepository bookRepository) {
        this.bookRepository = bookRepository;
    }

    public Book createBook(String title, String author, String isbn, Integer year) {
        Book book = new Book(title, author, isbn, year);
        return bookRepository.save(book); // INSERT или UPDATE
    }

    @Transactional(readOnly = true)
    public Optional<Book> getBook(Long id) {
        return bookRepository.findById(id);
    }

    @Transactional(readOnly = true)
    public List<Book> getAvailableBooks() {
        return bookRepository.findByAvailableTrue();
    }

    @Transactional(readOnly = true)
    public List<BookRepository.BookTitleAuthor> getRecentBookPreviews() {
        return bookRepository.findTop5ByAvailableTrueOrderByPublishedYearDesc();
    }

    public void markAsUnavailable(Long id) {
        bookRepository.findById(id)
            .ifPresent(book -> {
                book.setAvailable(false);
                // save() не требуется — изменения отслеживаются автоматически
            });
    }
}
