class Rectangle
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
  
  def square?
    @width == @height
  end
end

rect = Rectangle.new(10, 20)
puts rect.area      # 200
puts rect.perimeter # 60
puts rect.square?   # false
