class User {
    private let username: String
    private let password: String
    private var loggedIn = false

    init(username: String, password: String) {
        self.username = username
        self.password = password
    }

    func login(_ password: String) {
        if password == self.password {
            loggedIn = true
            print("Добро пожаловать, \(username)!")
        } else {
            print("Ошибка: неверный пароль")
        }
    }

    func logout() {
        loggedIn = false
        print("\(username) вышел из системы")
    }

    func postMessage(_ text: String) {
        if !loggedIn {
            print("Сначала войдите в систему")
            return
        }
        print("Сообщение опубликовано: \(text)")
    }
}

let user = User(username: "alex", password: "secret123")
user.postMessage("Привет!")
user.login("wrong")
user.login("secret123")
user.postMessage("Привет, мир!")
user.logout()
user.postMessage("Ещё одно сообщение")
