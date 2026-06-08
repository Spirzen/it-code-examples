use serde::{Deserialize, Serialize};
use std::fs;

#[derive(Debug, Serialize, Deserialize)]
struct Task {
    id: u64,
    title: String,
    done: bool,
}

const DB: &str = "tasks.json";

fn load() -> Vec<Task> {
    fs::read_to_string(DB)
        .ok()
        .and_then(|s| serde_json::from_str(&s).ok())
        .unwrap_or_default()
}

fn save(tasks: &[Task]) -> std::io::Result<()> {
    fs::write(DB, serde_json::to_string_pretty(tasks)?)
}

fn main() -> std::io::Result<()> {
    let mut tasks = load();
    tasks.push(Task {
        id: 1,
        title: "Изучить Rust".into(),
        done: false,
    });
    save(&tasks)?;
    Ok(())
}
