
import com.zaxxer.hikari.HikariConfig;
import com.zaxxer.hikari.HikariDataSource;

import javax.sql.DataSource;
import java.sql.*;
import java.time.Instant;
import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

public class JdbcBookRepository {

    private final DataSource dataSource;

    public JdbcBookRepository() {
        HikariConfig config = new HikariConfig();
        config.setJdbcUrl("jdbc:postgresql://localhost:5432/library");
        config.setUsername("user");
        config.setPassword("password");
        config.setMaximumPoolSize(10);
        // Автоматическое восстановление разорванных соединений
        config.setConnectionTestQuery("SELECT 1");
        this.dataSource = new HikariDataSource(config);
    }

    // Создание книги
    public Book save(Book book) {
        String sql = """
            INSERT INTO books (title, author, isbn, published_year, available)
            VALUES (?, ?, ?, ?, ?)
            RETURNING id
            """;

        try (Connection conn = dataSource.getConnection();
             PreparedStatement stmt = conn.prepareStatement(sql, Statement.RETURN_GENERATED_KEYS)) {

            stmt.setString(1, book.getTitle());
            stmt.setString(2, book.getAuthor());
            stmt.setString(3, book.getIsbn());
            stmt.setInt(4, book.getPublishedYear());
            stmt.setBoolean(5, book.getAvailable() != null ? book.getAvailable() : true);

            int affectedRows = stmt.executeUpdate();
            if (affectedRows == 0) {
                throw new SQLException("Создание книги не привело к вставке данных.");
            }

            try (ResultSet generatedKeys = stmt.getGeneratedKeys()) {
                if (generatedKeys.next()) {
                    book.setId(generatedKeys.getLong(1));
                } else {
                    throw new SQLException("Не удалось получить сгенерированный ID.");
                }
            }

            return book;

        } catch (SQLException e) {
            throw new RuntimeException("Ошибка при сохранении книги", e);
        }
    }

    // Чтение по ID
    public Optional<Book> findById(Long id) {
        String sql = "SELECT id, title, author, isbn, published_year, available FROM books WHERE id = ?";

        try (Connection conn = dataSource.getConnection();
             PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setLong(1, id);
            try (ResultSet rs = stmt.executeQuery()) {
                if (rs.next()) {
                    return Optional.of(mapRow(rs));
                }
                return Optional.empty();
            }

        } catch (SQLException e) {
            throw new RuntimeException("Ошибка при поиске книги по ID", e);
        }
    }

    // Чтение всех доступных книг
    public List<Book> findAllAvailable() {
        String sql = "SELECT id, title, author, isbn, published_year, available FROM books WHERE available = true";

        try (Connection conn = dataSource.getConnection();
             PreparedStatement stmt = conn.prepareStatement(sql);
             ResultSet rs = stmt.executeQuery()) {

            List<Book> books = new ArrayList<>();
            while (rs.next()) {
                books.add(mapRow(rs));
            }
            return books;

        } catch (SQLException e) {
            throw new RuntimeException("Ошибка при получении списка книг", e);
        }
    }

    // Обновление
    public boolean update(Book book) {
        String sql = """
            UPDATE books
            SET title = ?, author = ?, isbn = ?, published_year = ?, available = ?
            WHERE id = ?
            """;

        try (Connection conn = dataSource.getConnection();
             PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setString(1, book.getTitle());
            stmt.setString(2, book.getAuthor());
            stmt.setString(3, book.getIsbn());
            stmt.setInt(4, book.getPublishedYear());
            stmt.setBoolean(5, book.getAvailable());
            stmt.setLong(6, book.getId());

            return stmt.executeUpdate() > 0;

        } catch (SQLException e) {
            throw new RuntimeException("Ошибка при обновлении книги", e);
        }
    }

    // Удаление
    public boolean deleteById(Long id) {
        String sql = "DELETE FROM books WHERE id = ?";
        try (Connection conn = dataSource.getConnection();
             PreparedStatement stmt = conn.prepareStatement(sql)) {
            stmt.setLong(1, id);
            return stmt.executeUpdate() > 0;
        } catch (SQLException e) {
            throw new RuntimeException("Ошибка при удалении книги", e);
        }
    }

    // Вспомогательный метод: ResultSet → Book
    private Book mapRow(ResultSet rs) throws SQLException {
        Book book = new Book();
        book.setId(rs.getLong("id"));
        book.setTitle(rs.getString("title"));
        book.setAuthor(rs.getString("author"));
        book.setIsbn(rs.getString("isbn"));
        book.setPublishedYear(rs.getInt("published_year"));
        book.setAvailable(rs.getBoolean("available"));
        return book;
    }
}
