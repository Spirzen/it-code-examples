abstract type Shape end

struct Circle <: Shape
    r::Float64
end

struct Rect <: Shape
    w::Float64
    h::Float64
end

area(s::Circle) = π * s.r^2
area(s::Rect) = s.w * s.h

area(Circle(2.0))   # ≈ 12.57
area(Rect(3.0, 4.0)) # 12.0
