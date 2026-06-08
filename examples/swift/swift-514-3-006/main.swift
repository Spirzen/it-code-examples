struct URLRequestBuilder {
    var url: URL?
    var method: String = "GET"
    var headers: [String: String] = [:]

    func setURL(_ url: URL) -> Self {
        var copy = self
        copy.url = url
        return copy
    }

    func build() throws -> URLRequest {
        guard let url = url else { throw URLError(.badURL) }
        var request = URLRequest(url: url)
        request.httpMethod = method
        request.allHTTPHeaderFields = headers
        return request
    }
}
