class Calculator {
    func add(_ a: Int, _ b: Int) -> Int {
        return a + b
    }
    
    func add(_ a: Double, _ b: Double) -> Double {
        return a + b
    }
    
    func add(_ numbers: Int...) -> Int {
        return numbers.reduce(0, +)
    }
    
    func add(_ a: String, _ b: String) -> String {
        return a + b
    }
}

class Logger {
    func log(_ message: String) {
        print("[INFO] \(message)")
    }
    
    func log(_ message: String, level: String) {
        print("[\(level)] \(message)")
    }
    
    func log(_ message: String, file: String, line: Int) {
        print("[\(file):\(line)] \(message)")
    }
    
    func log(error: Error) {
        print("[ERROR] \(error.localizedDescription)")
    }
}
