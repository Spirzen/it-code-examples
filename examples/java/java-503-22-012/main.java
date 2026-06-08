public class Book {
    private Long id;
    private String title;
    private String author;
    private String isbn;
    private Integer publishedYear;
    private Boolean available;

    // конструкторы, геттеры, сеттеры
    public Book() {}

    public Book(String title, String author, String isbn, Integer publishedYear) {
        this.title = title;
        this.author = author;
        this.isbn = isbn;
        this.publishedYear = publishedYear;
        this.available = true;
    }

    // ... геттеры и сеттеры
}
