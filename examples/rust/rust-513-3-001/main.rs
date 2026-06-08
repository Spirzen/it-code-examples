impl User {
    fn new(email: String, username: String) -> User {
        User {
            email,
            username,
            active: true,
            sign_in_count: 1,
        }
    }

    fn greet(&self) -> String {
        format!("Hello, {}!", self.username)
    }

    fn activate(&mut self) {
        self.active = true;
    }
}
