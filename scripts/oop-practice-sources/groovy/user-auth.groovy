class User {
    private String username
    private String password
    private boolean loggedIn

    User(String username, String password) {
        this.username = username
        this.password = password
        this.loggedIn = false
    }

    void login(String password) {
        if (password == this.password) {
            loggedIn = true
            println "Добро пожаловать, ${username}!"
        } else {
            println 'Ошибка: неверный пароль'
        }
    }

    void logout() {
        loggedIn = false
        println "${username} вышел из системы"
    }

    void postMessage(String text) {
        if (!loggedIn) {
            println 'Сначала войдите в систему'
            return
        }
        println "Сообщение опубликовано: ${text}"
    }
}

def user = new User('alex', 'secret123')
user.postMessage('Привет!')
user.login('wrong')
user.login('secret123')
user.postMessage('Привет, мир!')
user.logout()
user.postMessage('Ещё одно сообщение')
