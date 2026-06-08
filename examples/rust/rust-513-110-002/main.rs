// src-tauri/src/main.rs
use tauri::command;

#[command]
fn greet(name: &str) -> String {
    format!("Привет, {}!", name)
}

fn main() {
    tauri::Builder::default()
        .invoke_handler(tauri::generate_handler![greet])
        .run(tauri::generate_context!())
        .expect("Ошибка при запуске приложения");
}
