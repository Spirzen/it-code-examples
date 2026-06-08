enum Message {
    Quit,
    Move { x: i32, y: i32 },
    Write(String),
    ChangeColor(i32, i32, i32),
}

fn handle_message(msg: Message) {
    match msg {
        Message::Quit => println!("Выход"),
        Message::Move { x, y } => println!("Перемещение в ({}, {})", x, y),
        Message::Write(text) => println!("Текст: {}", text),
        Message::ChangeColor(r, g, b) => println!("Цвет: R{} G{} B{}", r, g, b),
    }
}
