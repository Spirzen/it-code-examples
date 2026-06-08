struct Rectangle {
    var origin: Point
    var size: Size
    
    var area: Double {
        return size.width * size.height
    }
    
    var center: Point {
        return Point(
            x: origin.x + size.width / 2,
            y: origin.y + size.height / 2
        )
    }
}

struct RGBColor {
    var red: UInt8
    var green: UInt8
    var blue: UInt8
    
    var grayscale: UInt8 {
        return UInt8(Double(red) * 0.299 + Double(green) * 0.587 + Double(blue) * 0.114)
    }
}
