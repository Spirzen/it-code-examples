
import Foundation

struct Task: Codable {
    var id: UUID
    var title: String
    var done: Bool
}

struct TaskStore {
    let url: URL
    func load() -> [Task] {
        guard let data = try? Data(contentsOf: url),
              let tasks = try? JSONDecoder().decode([Task].self, from: data) else { return [] }
        return tasks
    }
    func save(_ tasks: [Task]) throws {
        let data = try JSONEncoder().encode(tasks)
        try data.write(to: url)
    }
}
