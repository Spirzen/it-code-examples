pub struct HttpRequest {
    method: Method,
    path: String,
    headers: HashMap<String, String>,
    body: Option<Vec<u8>>,
}

pub struct RequestBuilder {
    method: Method,
    path: String,
    headers: HashMap<String, String>,
    body: Option<Vec<u8>>,
}

impl RequestBuilder {
    pub fn new(method: Method, path: String) -> Self {
        Self {
            method,
            path,
            headers: HashMap::new(),
            body: None,
        }
    }
    
    pub fn header(mut self, name: &str, value: &str) -> Self {
        self.headers.insert(name.to_string(), value.to_string());
        self
    }
    
    pub fn body(mut self, body: Vec<u8>) -> Self {
        self.body = Some(body);
        self
    }
    
    pub fn build(self) -> HttpRequest {
        HttpRequest {
            method: self.method,
            path: self.path,
            headers: self.headers,
            body: self.body,
        }
    }
}

// Использование
let request = RequestBuilder::new(Method::POST, "/api/users")
    .header("Content-Type", "application/json")
    .header("Authorization", "Bearer token")
    .body(json_data)
    .build();
