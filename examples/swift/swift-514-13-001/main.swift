var nickname: String? = nil
nickname = "swift_dev"

if let nick = nickname {
    print("Ник: \(nick)")    // nick — обычный String внутри блока
}

let displayName = nickname ?? "Гость"

func requireName(_ value: String?) -> String {
    guard let name = value, !name.isEmpty else {
        return "Не указано"
    }
    return name
}
