struct UserProfile: Codable {
    let id: Int
    let name: String
    let age: Int
    let email: String?
}

func decodeProfile(from data: Data) throws -> UserProfile {
    try JSONDecoder().decode(UserProfile.self, from: data)
}

func label(for profile: UserProfile) -> String {
    if let email = profile.email {
        return "\(profile.name), \(profile.age) лет, \(email)"
    }
    return "\(profile.name), \(profile.age) лет"
}
