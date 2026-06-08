function make_counter()
    local count = 0
    return function()
        count = count + 1
        return count
    end
end

c1 = make_counter()
c2 = make_counter()

print(c1())  --> 1
print(c1())  --> 2
print(c2())  --> 1
