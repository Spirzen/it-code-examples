fn find_port(name: &str) -> Option<u16> {
    match name {
        "http" => Some(80),
        "https" => Some(443),
        _ => None,
    }
}

fn main() {
    match find_port("https") {
        Some(p) => println!("порт {p}"),
        None => println!("порт неизвестен"),
    }
}
