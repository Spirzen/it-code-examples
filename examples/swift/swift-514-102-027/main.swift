class DatabaseManager {
    static let shared = DatabaseManager()
    
    func connect() {
        print("Подключение к базе данных")
    }
    
    func disconnect() {
        print("Отключение от базы данных")
    }
    
    func execute(query: String) -> [String: Any] {
        print("Выполнение запроса: \(query)")
        return [:]
    }
}

struct CacheEntry {
    let key: String
    let value: Any
    let timestamp: Date
    
    func isExpired(after seconds: TimeInterval) -> Bool {
        return Date().timeIntervalSince(timestamp) > seconds
    }
}

enum AppErrorKind {
    case network
    case database
    case validation
    case unknown
    
    var description: String {
        switch self {
        case .network: return "Ошибка сети"
        case .database: return "Ошибка базы данных"
        case .validation: return "Ошибка валидации"
        case .unknown: return "Неизвестная ошибка"
        }
    }
}
