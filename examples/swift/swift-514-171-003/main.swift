enum AuthError: Error, LocalizedError {
    case wrongPassword
    case accountLocked(until: Date)

    var errorDescription: String? {
        switch self {
        case .wrongPassword:
            return "Неверный пароль"
        case .accountLocked(let until):
            return "Аккаунт заблокирован до \(until.formatted())"
        }
    }
}

func signIn(password: String) throws {
    if password != "secret" { throw AuthError.wrongPassword }
}
