#[derive(Debug)]
struct Config {
    port: u16,
}

fn main() {
    let cfg = Config { port: 8080 };

    let doubled = {
        let base = 21;
        base * 2 // без `;` — блок возвращает 42
    };

    println!("{:?}, doubled={}", cfg, doubled);
}
