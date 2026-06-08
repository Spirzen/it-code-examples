use std::sync::mpsc;
use std::thread;

fn main() {
    let (tx, rx) = mpsc::channel();

    thread::spawn(move || {
        tx.send("готово".to_string()).unwrap();
    });

    match rx.recv() {
        Ok(msg) => println!("{msg}"),
        Err(_) => println!("отправитель отключился"),
    }
}
