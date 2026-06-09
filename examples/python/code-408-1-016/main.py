class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password  # Скрытый пароль
        self.is_logged_in = False

    def login(self, password_attempt):
        if password_attempt == self.__password:
            self.is_logged_in = True
            print(f"✅ {self.username}, добро пожаловать!")
            return True
        else:
            print(f"❌ Неверный пароль для {self.username}")
            return False

    def logout(self):
        self.is_logged_in = False
        print(f"{self.username} вышел из системы")

    def post_message(self, message):
        if self.is_logged_in:
            print(f"{self.username}: {message}")
        else:
            print("Пожалуйста, войдите в систему!")


# Использование
user1 = User("Алексей", "qwerty123")
user2 = User("Мария", "pass456")

user1.post_message("Привет!")  # Пожалуйста, войдите в систему!

user1.login("wrong")     # ❌ Неверный пароль
user1.login("qwerty123") # ✅ Алексей, добро пожаловать!
user1.post_message("Всем привет!")  # Алексей: Всем привет!

user2.login("pass456")
user2.post_message("Привет, Алексей!")
