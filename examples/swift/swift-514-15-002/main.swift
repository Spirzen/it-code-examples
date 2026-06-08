protocol HTTPClient {
    func data(from url: URL) async throws -> Data
}

struct URLSessionClient: HTTPClient {
    func data(from url: URL) async throws -> Data {
        try await URLSession.shared.data(from: url).0
    }
}

struct UserService {
    let client: HTTPClient
    func fetchUsers() async throws -> [UserDTO] {
        let url = URL(string: "https://api.example.com/users")!
        let data = try await client.data(from: url)
        return try JSONDecoder().decode([UserDTO].self, from: data)
    }
}
