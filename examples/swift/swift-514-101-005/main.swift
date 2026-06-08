func loadUserProfile() async throws -> UserProfile {
    let userData = try await networkService.fetch(endpoint: .profile)
    let avatarData = try await imageService.load(url: userData.avatarURL)
    return UserProfile(userData: userData, avatar: avatarData)
}

// Использование
Task {
    do {
        let profile = try await loadUserProfile()
        display(profile)
    } catch {
        showError(error)
    }
}
