from cryptography.fernet import Fernet

# Генерация ключа
key = Fernet.generate_key()
cipher = Fernet(key)

# Исходный текст
plaintext = b"Secret message"
print(f"Открытый текст: {plaintext.decode()}")

# Шифрование
ciphertext = cipher.encrypt(plaintext)
print(f"Шифротекст: {ciphertext}")

# Расшифрование
decrypted = cipher.decrypt(ciphertext)
print(f"Расшифрованный текст: {decrypted.decode()}")
