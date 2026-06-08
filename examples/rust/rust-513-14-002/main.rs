fn classify(score: u32) -> &'static str {
    if score >= 90 {
        "отлично"
    } else if score >= 75 {
        "хорошо"
    } else {
        "нужно подтянуть"
    }
}

fn main() {
    let label = classify(82);
    println!("Результат: {}", label);
}
