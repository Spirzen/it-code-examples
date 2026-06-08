struct Point {
    var x: Int
    var y: Int
}

class Session {
    var token: String
    init(token: String) { self.token = token }
}

var p1 = Point(x: 0, y: 0)
var p2 = p1
p2.x = 10
// p1.x остаётся 0 — независимые копии

let s1 = Session(token: "abc")
let s2 = s1
s2.token = "xyz"
// s1.token тоже "xyz" — одна ссылка на объект
