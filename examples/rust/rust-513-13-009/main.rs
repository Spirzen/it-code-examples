#[derive(Debug)]
struct Person {
    name: String,
    age: u8,
}

enum Contact {
    Email(String),
    Phone(String),
}

fn main() {
    let person = Person {
        name: String::from("Анна"),
        age: 30,
    };

    let contact = Contact::Email(String::from("anna@example.com"));

    println!("{:?}", person);

    match contact {
        Contact::Email(addr) => println!("Электронная почта: {}", addr),
        Contact::Phone(num) => println!("Телефон: {}", num),
    }
}
