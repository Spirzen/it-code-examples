local User = {}

function User:new(username, email)
    if not username or #username < 3 then
        error("Имя пользователя должно быть не короче 3 символов")
    end
    if not string.match(email, "@") then
        error("Некорректный формат email")
    end
    
    local user = setmetatable({}, {__index = self})
    user.username = username
    user.email = email
    user.isActive = true
    return user
end
