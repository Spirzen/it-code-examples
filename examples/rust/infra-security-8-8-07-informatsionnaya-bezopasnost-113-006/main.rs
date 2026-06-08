use axum::{
    response::{IntoResponse, Response},
    middleware::{self, Next},
    http::Request,
};

async fn security_headers<B>(req: Request<B>, next: Next<B>) -> Response {
    let mut res = next.run(req).await.into_response();
    res.headers_mut().insert(
        axum::http::header::CONTENT_SECURITY_POLICY,
        "default-src 'self'".parse().unwrap(),
    );
    res
}
