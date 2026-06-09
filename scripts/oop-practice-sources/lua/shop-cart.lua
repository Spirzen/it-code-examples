local Product = {}

function Product:new(name, price)
    local obj = setmetatable({name = name, price = price}, {__index = self})
    return obj
end

local Cart = {}

function Cart:new()
    local obj = setmetatable({items = {}}, {__index = self})
    return obj
end

function Cart:add(product)
    table.insert(self.items, product)
    print("В корзину добавлено: " .. product.name .. " (" .. product.price .. " ₽)")
end

function Cart:total()
    local sum = 0
    for _, p in ipairs(self.items) do
        sum = sum + p.price
    end
    return sum
end

local Order = {}

function Order:new(cart)
    local items = {}
    for _, item in ipairs(cart.items) do
        table.insert(items, item)
    end
    local obj = setmetatable({items = items, total = cart:total()}, {__index = self})
    return obj
end

function Order:checkout()
    print("Оформление заказа...")
    for _, item in ipairs(self.items) do
        print("  — " .. item.name .. ": " .. item.price .. " ₽")
    end
    print("Итого: " .. self.total .. " ₽")
    print("Заказ оформлен!")
end

local cart = Cart:new()
cart:add(Product:new("Книга", 500))
cart:add(Product:new("Ручка", 50))
local order = Order:new(cart)
order:checkout()
