public class NetworkManager {
    public static let shared = NetworkManager()
    
    public func fetchData(from url: String, completion: @escaping (Data?) -> Void) {
        // Реализация загрузки данных
        print("Загрузка данных с \(url)")
        completion(nil)
    }
    
    public func uploadData(_ data: Data, to url: String, completion: @escaping (Bool) -> Void) {
        // Реализация загрузки данных
        print("Отправка данных на \(url)")
        completion(true)
    }
}

public struct User {
    public let id: Int
    public let name: String
    public let email: String
    
    public init(id: Int, name: String, email: String) {
        self.id = id
        self.name = name
        self.email = email
    }
    
    public func displayName() -> String {
        return name
    }
}
