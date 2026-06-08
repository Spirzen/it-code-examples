#[tokio::test]
async fn create_note_returns_json() {
    let state = test_state();
    let app = app(state);

    let response = app
        .oneshot(
            Request::builder()
                .method("POST")
                .uri("/notes")
                .header("content-type", "application/json")
                .body(Body::from(r#"{"text":"тест"}"#))
                .unwrap(),
        )
        .await
        .unwrap();

    assert_eq!(StatusCode::CREATED, response.status());

    let bytes = response.into_body().collect().await.unwrap().to_bytes();
    let note: Note = serde_json::from_slice(&bytes).unwrap();
    assert_eq!("тест", note.text);
}
