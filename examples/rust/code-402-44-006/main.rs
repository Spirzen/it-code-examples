enum Option<T> {
    Some(T),
    None,
}

fn find_user(id: u32) -> Option<User> {
    if database.contains(id) {
        Some(database.get(id))
    } else {
        None
    }
}

match find_user(42) {
    Some(user) => println!("Найден: {}", user.name),
    None => println!("Пользователь не найден"),
}
