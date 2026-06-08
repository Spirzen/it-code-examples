// Create
def book = new Book(title: 'Groovy in Action', author: 'Dierk König', price: 49.99G)
book.save(failOnError: true)

// Read
Book book = Book.get(1L)
List<Book> cheap = Book.findAllByPriceLessThan(50.0G)

// Update
book.price = 39.99G
book.save()

// Delete
book.delete()
