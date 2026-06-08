type
  ShapeKind = enum
    skCircle, skRectangle

  Shape = object
    kind: ShapeKind
    case kind
    of skCircle:
      radius: float
    of skRectangle:
      width, height: float

proc area(s: Shape): float =
  case s.kind
  of skCircle:
    return 3.14159 * s.radius * s.radius
  of skRectangle:
    return s.width * s.height

let circle = Shape(kind: skCircle, radius: 5.0)
let rect = Shape(kind: skRectangle, width: 4.0, height: 6.0)

echo "Площадь круга: ", area(circle)
echo "Площадь прямоугольника: ", area(rect)
