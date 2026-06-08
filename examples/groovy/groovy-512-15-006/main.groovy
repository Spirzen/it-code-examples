@groovy.transform.CompileStatic
class CatalogService {
    private final List<CatalogBook> books

    CatalogService(List<CatalogBook> books) {
        this.books = books
    }

    List<CatalogBook> activeBooks() {
        books.findAll { it.active }
    }

    BigDecimal totalPrice() {
        activeBooks().collect { it.price }.inject(0G) { a, b -> a + b }
    }
}
