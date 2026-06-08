protocol Flyable {
    func fly()
    var maxAltitude: Double { get }
}

protocol Swimmable {
    func swim()
    var maxDepth: Double { get }
}

class Duck: Animal, Flyable, Swimmable {
    var maxAltitude: Double = 1000.0
    var maxDepth: Double = 10.0
    
    func fly() {
        print("Утка летит")
    }
    
    func swim() {
        print("Утка плавает")
    }
}
