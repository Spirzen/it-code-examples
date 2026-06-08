struct Point {
    var x: Double
    var y: Double
    
    mutating func moveBy(x deltaX: Double, y deltaY: Double) {
        x += deltaX
        y += deltaY
    }
    
    mutating func reset() {
        x = 0.0
        y = 0.0
    }
}
