struct User {
    username: String,
    password: String,
    logged_in: bool,
}

impl User {
    fn new(username: &str, password: &str) -> Self {
        Self {
            username: username.to_string(),
            password: password.to_string(),
            logged_in: false,
        }
    }

    fn login(&mut self, password: &str) {
        if password == self.password {
            self.logged_in = true;
            println!("Добро пожаловать, {}!", self.username);
        } else {
            println!("Ошибка: неверный пароль");
        }
    }

    fn logout(&mut self) {
        self.logged_in = false;
        println!("{} вышел из системы", self.username);
    }

    fn post_message(&self, text: &str) {
        if !self.logged_in {
            println!("Сначала войдите в систему");
            return;
        }
        println!("Сообщение опубликовано: {}", text);
    }
}

fn main() {
    let mut user = User::new("alex", "secret123");
    user.post_message("Привет!");
    user.login("wrong");
    user.login("secret123");
    user.post_message("Привет, мир!");
    user.logout();
    user.post_message("Ещё одно сообщение");
}
