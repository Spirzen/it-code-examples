fn main() {
    let mut numbers = vec![1, 2, 3];

    // Ссылка для чтения
    let read_ref = &numbers;

    // Попытка получить ссылку для записи вызовет ошибку
    // because a mutable reference cannot exist while an immutable one exists
    // let write_ref = &mut numbers; 

    println!("Чтение через immutable ссылку: {:?}", read_ref);

    // После выхода read_ref из области видимости можно писать
    let write_ref = &mut numbers;
    write_ref.push(4);

    println!("После изменения: {:?}", numbers);
}
