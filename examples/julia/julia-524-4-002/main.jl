# 1) Проверка подтипов
Int64 <: Integer
Integer <: Number
Number <: Any

# 2) Определение типа выражения
typeof(1 // 2)          # Rational
typeof(1 + 2im)         # Complex
typeof((1, "x", 2.0))   # Tuple{Int64, String, Float64}

# 3) Стабильность контейнеров
a = Int[]
push!(a, 1)
# push!(a, "x")         # MethodError: защищает от смешивания типов
