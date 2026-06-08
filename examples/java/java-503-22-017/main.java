
import org.springframework.Data.jpa.repository.*;
import org.springframework.Data.repository.query.Param;

import java.util.List;
import java.util.Optional;

public interface BookRepository extends JpaRepository<Book, Long> {

    // Генерация по имени метода
    List<Book> findByAvailableTrue();
    List<Book> findByAuthorAndPublishedYear(String author, Integer year);
    Optional<Book> findByIsbn(String isbn);

    // Проекция: интерфейс
    interface BookTitleAuthor {
        String getTitle();
        String getAuthor();
    }

    // Возврат проекции
    List<BookTitleAuthor> findTop5ByAvailableTrueOrderByPublishedYearDesc();

    // Явный JPQL
    @Query("SELECT b FROM Book b WHERE LOWER(b.title) LIKE LOWER(CONCAT('%', :query, '%'))")
    List<Book> searchByTitleFragment(@Param("query") String query);

    // Нативный SQL (осторожно!)
    @Query(value = """
        SELECT b.*, COUNT(r.id) as reservation_count
        FROM books b
        LEFT JOIN reservations r ON b.id = r.book_id AND r.status = 'ACTIVE'
        GROUP BY b.id
        HAVING COUNT(r.id) < :maxReservations
        """, nativeQuery = true)
    List<Object[]> findBooksUnderReservationLimit(@Param("maxReservations") int maxReservations);
}
