# Python (плохой пример)
class UserManager:
    def save_user(self, user_data):
        with open("users.txt", "a") as f:
            f.write(f"{user_data}\n")
    
    def send_email(self, email, message):
        # Логика отправки email
        print(f"Sending email to {email}: {message}")
