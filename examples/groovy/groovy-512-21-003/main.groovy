class CatalogServiceSpec extends Specification {
    def "фильтрует только активные книги"() {
        given:
        def service = new CatalogService([
            new CatalogBook(title: "A", active: true,  price: 10G),
            new CatalogBook(title: "B", active: false, price: 20G)
        ])

        when:
        def result = service.activeBooks()

        then:
        result*.title == ["A"]
    }
}
