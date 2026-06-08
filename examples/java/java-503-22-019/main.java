
import org.springframework.Data.annotation.Id;
import org.springframework.Data.relational.core.mapping.Table;

@Table("books")
public record Book(
    @Id Long id,
    String title,
    String author,
    String isbn,
    Integer publishedYear,
    Boolean available
) {
    public Book(String title, String author, String isbn, Integer publishedYear) {
        this(null, title, author, isbn, publishedYear, true);
    }
}
