struct Point {
    var x: Double
    var y: Double
    
    mutating func moveBy(dx: Double, dy: Double) {
        x += dx
        y += dy
    }
}

var point1 = Point(x: 0.0, y: 0.0)
var point2 = point1

point2.moveBy(dx: 5.0, dy: 5.0)

print("point1: (\(point1.x), \(point1.y))") // (0.0, 0.0)
print("point2: (\(point2.x), \(point2.y))") // (5.0, 5.0)

func modifyPoint(_ point: inout Point) {
    point.moveBy(dx: 10.0, dy: 10.0)
}

modifyPoint(&point1)
print("point1 после модификации: (\(point1.x), \(point1.y))") // (10.0, 10.0)
