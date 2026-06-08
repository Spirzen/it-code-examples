use axum::{
    extract::{Path, State},
    http::StatusCode,
    routing::{delete, get, post},
    Json, Router,
};
use serde::{Deserialize, Serialize};
use std::sync::{Arc, Mutex};

#[derive(Clone, Serialize)]
struct Note {
    id: u32,
    text: String,
}

#[derive(Deserialize)]
struct NoteCreate {
    text: String,
}

type AppState = Arc<Mutex<(Vec<Note>, u32)>>;

#[tokio::main]
async fn main() {
    let state: AppState = Arc::new(Mutex::new((Vec::new(), 1)));

    let app = Router::new()
        .route("/health", get(health))
        .route("/notes", get(list_notes).post(create_note))
        .route("/notes/:id", delete(delete_note))
        .with_state(state);

    let listener = tokio::net::TcpListener::bind("0.0.0.0:3000")
        .await
        .unwrap();
    println!("http://127.0.0.1:3000");
    axum::serve(listener, app).await.unwrap();
}

async fn health() -> &'static str {
    "ok"
}

async fn list_notes(State(state): State<AppState>) -> Json<Vec<Note>> {
    let guard = state.lock().unwrap();
    Json(guard.0.clone())
}

async fn create_note(
    State(state): State<AppState>,
    Json(body): Json<NoteCreate>,
) -> (StatusCode, Json<Note>) {
    let mut guard = state.lock().unwrap();
    let id = guard.1;
    guard.1 += 1;
    let note = Note {
        id,
        text: body.text,
    };
    guard.0.push(note.clone());
    (StatusCode::CREATED, Json(note))
}

async fn delete_note(
    State(state): State<AppState>,
    Path(id): Path<u32>,
) -> StatusCode {
    let mut guard = state.lock().unwrap();
    let len_before = guard.0.len();
    guard.0.retain(|n| n.id != id);
    if guard.0.len() < len_before {
        StatusCode::NO_CONTENT
    } else {
        StatusCode::NOT_FOUND
    }
}
