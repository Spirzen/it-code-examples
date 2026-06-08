use std::io::{self, Write};

fn calc(a: f64, b: f64, op: char) -> Result<f64, String> {
    Ok(match op {
        '+' => a + b,
        '-' => a - b,
        '*' => a * b,
        '/' if b == 0.0 => return Err("деление на ноль".into()),
        '/' => a / b,
        _ => return Err(format!("неизвестный оператор: {op}")),
    })
}

fn main() -> io::Result<()> {
    let stdin = io::stdin();
    loop {
        print!("a op b (q): ");
        io::stdout().flush()?;
        let mut line = String::new();
        stdin.read_line(&mut line)?;
        let line = line.trim();
        if line == "q" { break; }
        let mut parts = line.split_whitespace();
        let a: f64 = parts.next().ok_or("a?")?.parse().map_err(|_| "a?")?;
        let op = parts.next().ok_or("op?")?.chars().next().ok_or("op?")?;
        let b: f64 = parts.next().ok_or("b?")?.parse().map_err(|_| "b?")?;
        match calc(a, b, op) {
            Ok(v) => println!("= {v}"),
            Err(e) => eprintln!("{e}"),
        }
    }
    Ok(())
}
