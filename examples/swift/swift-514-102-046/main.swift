class Document {
    let identifier: UUID
    var content: String
    var lastModified: Date
    
    init(content: String) {
        self.identifier = UUID()
        self.content = content
        self.lastModified = Date()
    }
    
    func save() {
        lastModified = Date()
        // Сохранение документа
    }
}

class NetworkSession {
    private let session: URLSession
    private var activeTasks: [URLSessionTask] = []
    
    init(configuration: URLSessionConfiguration) {
        self.session = URLSession(configuration: configuration)
    }
    
    func fetchData(from url: URL, completion: @escaping (Data?, Error?) -> Void) {
        let task = session.dataTask(with: url, completionHandler: completion)
        activeTasks.append(task)
        task.resume()
    }
    
    func cancelAllTasks() {
        activeTasks.forEach { $0.cancel() }
        activeTasks.removeAll()
    }
}
