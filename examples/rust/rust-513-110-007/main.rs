use hyper::{Body, Request, Response, Server};
use hyper::service::{make_service_fn, service_fn};
use std::convert::Infallible;

async fn handle(_req: Request<Body>) -> Result<Response<Body>, Infallible> {
    Ok(Response::new(Body::from("Привет из Hyper!")))
}

#[tokio::main]
async fn main() {
    let make_svc = make_service_eq!(|| async { Ok::<_, Infallible>(service_fn(handle)) });
    let addr = ([127, 0, 0, 1], 3000).into();
    let server = Server::bind(&addr).serve(make_svc);
    server.await.unwrap();
}
