class Apartment {
    let unit: String
    weak var tenant: Person?
    
    init(unit: String) {
        self.unit = unit
    }
}

class PersonWithApartment {
    let name: String
    var apartment: Apartment?
    
    init(name: String) {
        self.name = name
    }
    
    deinit {
        print("\(name) освобождает квартиру")
    }
}

var person: PersonWithApartment? = PersonWithApartment(name: "Мария")
var apartment: Apartment? = Apartment(unit: "42B")

person?.apartment = apartment
apartment?.tenant = person

person = nil
// Вывод: Мария освобождает квартиру
// Квартира автоматически теряет ссылку на жильца
