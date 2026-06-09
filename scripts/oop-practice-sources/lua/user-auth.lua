local User = {}

function User:new(username, password)
    local obj = setmetatable({
        username = username,
        _password = password,
        _logged_in = false
    }, {__index = self})
    return obj
end

function User:login(password)
    if password == self._password then
        self._logged_in = true
        print("Добро пожаловать, " .. self.username .. "!")
    else
        print("Ошибка: неверный пароль")
    end
end

function User:logout()
    self._logged_in = false
    print(self.username .. " вышел из системы")
end

function User:post_message(text)
    if not self._logged_in then
        print("Сначала войдите в систему")
        return
    end
    print("Сообщение опубликовано: " .. text)
end

local user = User:new("alex", "secret123")
user:post_message("Привет!")
user:login("wrong")
user:login("secret123")
user:post_message("Привет, мир!")
user:logout()
user:post_message("Ещё одно сообщение")
