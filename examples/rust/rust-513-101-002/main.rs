// Функция, требующая владения
fn take_ownership(value: String) {
    // value уничтожается при выходе из функции
}

// Функция, заимствующая данные для чтения
fn read_only(value: &String) {
    // value остаётся доступным после вызова
}

// Функция, заимствующая данные для изменения
fn modify(value: &mut String) {
    value.push_str("!");
}
