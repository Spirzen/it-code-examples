fn parse_port(s: &str) -> Result<u16, String> {
    let port: u16 = s.parse().map_err(|_| "порт должен быть числом".to_string())?;
    if port == 0 {
        return Err("порт не может быть 0".into());
    }
    Ok(port)
}

fn main() {
    for input in ["8080", "abc", "0"] {
        match parse_port(input) {
            Ok(p) => println!("{input} → {p}"),
            Err(e) => println!("{input}: {e}"),
        }
    }
}
