protocol Drawable {
    func draw()
}

protocol Serializable {
    func serialize() -> Data
}

class Renderer<T: Drawable> {
    func render(_ item: T) {
        item.draw()
    }
}

class Serializer<T: Serializable> {
    func serialize(_ item: T) -> Data {
        return item.serialize()
    }
}

class NetworkManager<T: Codable> {
    func send(_ item: T) throws {
        let data = try JSONEncoder().encode(item)
        // Отправка данных
        print("Отправлено \(payload.count) байт")
    }
    
    func receive(data: Data) throws -> T {
        return try JSONDecoder().decode(T.self, from: Data)
    }
}

class SortedArray<T: Comparable> {
    private var elements: [T] = []
    
    func insert(_ element: T) {
        let index = elements.firstIndex(where: { $0 > element }) ?? elements.count
        elements.insert(element, at: index)
    }
    
    func remove(_ element: T) -> Bool {
        if let index = elements.firstIndex(of: element) {
            elements.remove(at: index)
            return true
        }
        return false
    }
    
    var sortedElements: [T] {
        return elements
    }
}

struct Point: Comparable, Codable {
    var x: Double
    var y: Double
    
    static func < (lhs: Point, rhs: Point) -> Bool {
        return lhs.x < rhs.x || (lhs.x == rhs.x && lhs.y < rhs.y)
    }
}

let points = SortedArray<Point>()
points.insert(Point(x: 3.0, y: 4.0))
points.insert(Point(x: 1.0, y: 2.0))
print(points.sortedElements)
