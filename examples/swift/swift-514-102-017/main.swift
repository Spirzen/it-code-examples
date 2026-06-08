class Book {
    let title: String
    let author: String
    
    init(title: String, author: String) {
        self.title = title
        self.author = author
    }
}

let book1 = Book(title: "1984", author: "Джордж Оруэлл")
let book2 = book1
let book3 = Book(title: "1984", author: "Джордж Оруэлл")

print(book1 === book2) // true - одна и та же ссылка
print(book1 === book3) // false - разные объекты
print(book1 !== book3) // true - разные ссылки

if book1 === book2 {
    print("book1 и book2 ссылаются на один объект")
}
