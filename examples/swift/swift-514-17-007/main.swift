@MainActor
final class UsersViewModel: ObservableObject {
    @Published private(set) var users: [UserDTO] = []
    @Published private(set) var isLoading = false
    @Published private(set) var errorText: String?

    private let repository = UserRepository()
    private var activeTask: Task<Void, Never>?

    func reload() {
        activeTask?.cancel()
        activeTask = Task {
            isLoading = true
            defer { isLoading = false }
            do {
                let first = try await repository.user(id: 1)
                let second = try await repository.user(id: 2)
                if Task.isCancelled { return }
                users = [first, second]
            } catch is CancellationError {
                return
            } catch {
                errorText = error.localizedDescription
            }
        }
    }
}
