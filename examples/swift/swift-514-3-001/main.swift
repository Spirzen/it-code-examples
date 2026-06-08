struct Point {
    var x: Double
    var y: Double

    func distance(from other: Point) -> Double {
        let dx = x - other.x
        let dy = y - other.y
        return (dx * dx + dy * dy).squareRoot()
    }

    mutating func move(by deltaX: Double, deltaY: Double) {
        x += deltaX
        y += deltaY
    }
}
