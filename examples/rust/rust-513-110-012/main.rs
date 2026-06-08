use wiremock::{MockServer, Mock, ResponseTemplate};
use wiremock::matchers::{method, path};

#[tokio::test]
async fn test_http_client() {
    let mock_server = MockServer::start().await;
    Mock::given(method("GET"))
        .and(path("/api/user"))
        .respond_with(ResponseTemplate::new(200).set_body_json(json!({"name": "Алексей"})))
        .mount(&mock_server)
        .await;

    let client = reqwest::Client::new();
    let resp: serde_json::Value = client
        .get(format!("{}/api/user", mock_server.uri()))
        .send()
        .await
        .unwrap()
        .json()
        .await
        .unwrap();

    assert_eq!(resp["name"], "Алексей");
}
