use axum::{routing::get, Router};
use http_body_util::BodyExt;
use tower::ServiceExt;

#[tokio::test]
async fn health_returns_ok() {
    let app = Router::new().route("/health", get(|| async { "ok" }));

    let response = app
        .oneshot(
            axum::http::Request::builder()
                .uri("/health")
                .body(axum::body::Body::empty())
                .unwrap(),
        )
        .await
        .unwrap();

    assert_eq!(200, response.status());

    let body = response.into_body().collect().await.unwrap().to_bytes();
    assert_eq!(b"ok", body.as_ref());
}
