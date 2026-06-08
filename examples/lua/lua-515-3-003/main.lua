Vector = {}
Vector.__index = Vector

function Vector.new(x, y)
    return setmetatable({x = x or 0, y = y or 0}, Vector)
end

function Vector.__add(a, b)
    return Vector.new(a.x + b.x, a.y + b.y)
end

function Vector.__tostring(v)
    return "(" .. v.x .. ", " .. v.y .. ")"
end

v1 = Vector.new(1, 2)
v2 = Vector.new(3, 4)
v3 = v1 + v2
print(v3)  --> (4, 6)
