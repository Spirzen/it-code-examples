protocol Identifiable {
    var id: String { get }
    func generateID() -> String
}

protocol Loggable {
    func log(message: String)
    var logLevel: LogLevel { get set }
}

enum LogLevel {
    case debug, info, warning, error
}

class User: Identifiable, Loggable {
    var id: String
    var name: String
    var logLevel: LogLevel = .info
    
    init(id: String, name: String) {
        self.id = id
        self.name = name
    }
    
    func generateID() -> String {
        return UUID().uuidString
    }
    
    func log(message: String) {
        print("[\(logLevel)] \(name): \(message)")
    }
}

struct NetworkRequest: Identifiable {
    var id: String
    var url: String
    var method: String
    
    func generateID() -> String {
        return "\(method)-\(url.hashValue)"
    }
}
