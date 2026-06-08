class Shape
  def area
    0
  end
  
  def perimeter
    0
  end
  
  def description
    "Это геометрическая фигура"
  end
end

class Circle < Shape
  def initialize(radius)
    @radius = radius
  end
  
  def area
    Math::PI * @radius ** 2
  end
  
  def perimeter
    2 * Math::PI * @radius
  end
  
  def description
    "Это круг с радиусом #{@radius}"
  end
end

class Rectangle < Shape
  def initialize(width, height)
    @width = width
    @height = height
  end
  
  def area
    @width * @height
  end
  
  def perimeter
    2 * (@width + @height)
  end
  
  def description
    "Это прямоугольник #{@width}x#{@height}"
  end
end

circle = Circle.new(5)
rectangle = Rectangle.new(4, 6)

puts circle.area        # 78.53981633974483
puts circle.perimeter   # 31.41592653589793
puts circle.description # Это круг с радиусом 5

puts rectangle.area        # 24
puts rectangle.perimeter   # 20
puts rectangle.description # Это прямоугольник 4x6
