# Python (хороший пример)
class UserRepository:
    def save(self, user_data):
        with open("users.txt", "a") as f:
            f.write(f"{user_data}\n")

class EmailService:
    def send(self, email, message):
        print(f"Sending email to {email}: {message}")

class UserManager:
    def __init__(self, user_repo, email_service):
        self.user_repo = user_repo
        self.email_service = email_service
    
    def register_user(self, user_data, email):
        self.user_repo.save(user_data)
        self.email_service.send(email, "Welcome!")
