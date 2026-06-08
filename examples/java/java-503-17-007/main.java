class Book {
    private String title;
    private String author;
    
    public Book(String title, String author) {
        this.title = title;
        this.author = author;
    }
    
    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Book book = (Book) o;
        return title.equals(book.title) && author.equals(book.author);
    }
    
    @Override
    public int hashCode() {
        return Objects.hash(title, author);
    }
}

Book b1 = new Book("1984", "Оруэлл");
Book b2 = new Book("1984", "Оруэлл");
Book b3 = new Book("Мастер и Маргарита", "Булгаков");

System.out.println(b1.equals(b2));  // true
System.out.println(b1.equals(b3));  // false
System.out.println(b1.hashCode() == b2.hashCode());  // true — равные объекты имеют одинаковый хеш
