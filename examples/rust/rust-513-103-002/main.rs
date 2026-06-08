use std::fs;
use std::io;

fn sort_file(input: &str, output: &str) -> io::Result<()> {
    let mut lines: Vec<String> = fs::read_to_string(input)?
        .lines()
        .map(str::trim)
        .filter(|s| !s.is_empty())
        .map(String::from)
        .collect();
    lines.sort();
    fs::write(output, lines.join("\n") + "\n")?;
    Ok(())
}

fn main() -> io::Result<()> {
    sort_file("input.txt", "output.txt")?;
    println!("Готово: output.txt");
    Ok(())
}
