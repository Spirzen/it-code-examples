use testcontainers::{clients, images::postgres::Postgres, RunnableImage};

#[tokio::test]
async fn test_user_creation() {
    let docker = clients::Cli::default();
    let image = RunnableImage::from(Postgres::default()).with_tag("15");
    let node = docker.run(image);
    let port = node.get_host_port_ipv4(5432);

    let db_url = format!("postgres://postgres:postgres@localhost:{}/postgres", port);
    let db = Database::connect(db_url).await.unwrap();

    // Выполнение миграций и тестов
}
