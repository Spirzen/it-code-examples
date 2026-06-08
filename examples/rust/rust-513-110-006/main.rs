use actix_web::{web, App, HttpResponse, HttpServer, Result};

async fn greet(name: web::Path<String>) -> Result<HttpResponse> {
    Ok(HttpResponse::Ok().body(format!("Привет, {}!", name)))
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| {
        App::new().route("/greet/{name}", web::get().to(greet))
    })
    .bind("127.0.0.1:8080")?
    .run()
    .await
}
