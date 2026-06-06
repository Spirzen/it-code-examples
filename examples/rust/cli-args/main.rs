fn main() {
    let args: Vec<String> = std::env::args().collect();
    match args.len() {
        0..=1 => println!("usage: demo <name>"),
        _ => println!("Hello, {}!", args[1]),
    }
}
