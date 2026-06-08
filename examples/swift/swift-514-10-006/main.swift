// 1. Модель
struct UserDTO: Codable { let id: Int; let name: String }

// 2. Репозиторий (сеть + простой кэш)
final class UserRepository {
    func users() async throws -> [UserDTO] { /* URLSession + decode */ }
}

// 3. Экран
struct UsersView: View {
    @State private var users: [UserDTO] = []
    var body: some View {
        List(users, id: \.id) { Text($0.name) }
            .task { users = try await UserRepository().users() }
    }
}
