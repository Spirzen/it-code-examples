#![cfg_attr(
    all(not(debug_assertions), target_os = "windows"),
    windows_subsystem = "windows"
)]

use tauri::Manager;

#[tauri::command]
fn greet(name: &str) -> String {
    format!("Привет, {}! Текущее время: {}", name, chrono::Local::now().format("%H:%M:%S"))
}

fn main() {
    tauri::Builder::default()
        .invoke_handler(tauri::generate_handler![greet])
        .setup(|app| {
            // Дополнительная инициализация (например, проверка обновлений)
            Ok(())
        })
        .run(tauri::generate_context!())
        .expect("Ошибка запуска приложения");
}
