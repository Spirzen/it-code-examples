func fetchUser(id: String, completion: @escaping (Result<User, Error>) -> Void) {
    api.request(endpoint: .user(id)) { result in
        completion(result.map(User.init))
    }
}

// Использование
fetchUser(id: "123") { result in
    switch result {
    case .success(let user):
        self.display(user)
    case .failure(let error):
        self.showError(error)
    }
}
