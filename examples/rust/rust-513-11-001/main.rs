fn main() {
    let mut data = String::from("Исходные данные");

    {
        let ref1 = &data;
        let ref2 = &data;
        println!("data через ref1: {}", ref1);
        println!("data через ref2: {}", ref2);
        // let ref_mut = &mut data; // ошибка: пока живы ref1 и ref2
    } // immutable-заимствования закончились

    let ref_mut = &mut data;
    *ref_mut = String::from("Изменённые данные");
    println!("Изменённые данные: {}", data);
}
