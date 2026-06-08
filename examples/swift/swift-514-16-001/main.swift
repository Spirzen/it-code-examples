struct UserDTO: Codable {
    let id: Int
    let name: String
}

final class UserRepository {
    private let session: URLSession = .shared
    private var cache: [Int: UserDTO] = [:]

    func user(id: Int) async throws -> UserDTO {
        if let cached = cache[id] { return cached }
        let url = URL(string: "https://api.example.com/users/\(id)")!
        let (data, _) = try await session.data(from: url)
        let decoded = try JSONDecoder().decode(UserDTO.self, from: data)
        cache[id] = decoded
        return decoded
    }
}
