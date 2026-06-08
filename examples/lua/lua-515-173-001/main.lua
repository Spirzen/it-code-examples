local function divide(a, b)
    if b == 0 then
        error("division by zero")
    end
    return a / b
end

local ok, err = pcall(divide, 10, 0)

if ok then
    print("Result:", err)
else
    print("Error:", err)  --> Error: division by zero
end
