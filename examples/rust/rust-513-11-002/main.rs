// Функция пытается вернуть ссылку на локальную переменную x
// Это вызовет ошибку компилятора: "borrowed value does not live long enough"
fn invalid_reference() -> &String {
    let x = String::from("Временные данные");
    // Возврат ссылки на x недопустим, так как x будет удалён после выхода функции
    // return &x; 
    &x
}

// Корректный вариант: возврат самого значения по владению
fn valid_ownership() -> String {
    let x = String::from("Переданное владение");
    // Владелец передается вызывающей стороне, память останется валидной
    x
}

fn main() {
    // Вызов корректной функции передаёт владение
    let owned_string = valid_ownership();
    println!("{}", owned_string);

    // Попытка вызвать invalid_reference() приведёт к ошибке сборки
    // let broken_ref = invalid_reference(); 
}
