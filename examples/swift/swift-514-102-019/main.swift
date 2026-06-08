class Library {
    var books: [Book] = []
    var librarians: [Librarian] = []
    
    func addBook(_ book: Book) {
        books.append(book)
    }
    
    func addLibrarian(_ librarian: Librarian) {
        librarians.append(librarian)
    }
}

class University {
    var name: String
    var libraries: [Library] = []
    var departments: [Department] = []
    
    init(name: String) {
        self.name = name
    }
    
    func addLibrary(_ library: Library) {
        libraries.append(library)
    }
}
