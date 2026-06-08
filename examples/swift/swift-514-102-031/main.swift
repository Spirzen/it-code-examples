extension Loggable {
    func logDebug(_ message: String) {
        guard logLevel == .debug else { return }
        log(message: "[DEBUG] \(message)")
    }
    
    func logError(_ message: String) {
        logLevel = .error
        log(message: "[ERROR] \(message)")
    }
    
    mutating func setLogLevel(_ level: LogLevel) {
        logLevel = level
    }
}

extension Identifiable {
    func isValidID() -> Bool {
        return !id.isEmpty && id.count >= 5
    }
    
    func prefixID(with prefix: String) -> String {
        return "\(prefix)-\(id)"
    }
}

class Service: Loggable {
    var logLevel: LogLevel = .warning
    
    func log(message: String) {
        print("SERVICE LOG: \(message)")
    }
}

let service = Service()
service.logDebug("Начало обработки") // Не выводится при уровне .warning
service.logError("Критическая ошибка") // Выводится с изменением уровня
