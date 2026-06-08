
import random
import string

def generate_password(length=12):
    # Определение наборов символов
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation
    
    # Объединение всех наборов в одну строку
    all_chars = lowercase + uppercase + digits + symbols
    
    # Генерация случайного пароля заданной длины
    password = ''.join(random.choice(all_chars) for _ in range(length))
    
    return password

if __name__ == "__main__":
    user_length = int(input("Введите длину пароля: "))
    generated = generate_password(user_length)
    print(f"Сгенерированный пароль: {generated}")
