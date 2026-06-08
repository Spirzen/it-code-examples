
import hashlib

# Исходные данные
text = "Привет, мир!"
print(f"Исходный текст: {text}")

# Хеширование SHA-256
sha256_hash = hashlib.sha256(text.encode('utf-8')).hexdigest()
print(f"SHA-256: {sha256_hash}")

# Хеширование MD5
md5_hash = hashlib.md5(text.encode('utf-8')).hexdigest()
print(f"MD5: {md5_hash}")

# Хеширование файла
def hash_file(filename):
    sha256 = hashlib.sha256()
    with open(filename, 'rb') as f:
        while chunk := f.read(8192):
            sha256.update(chunk)
    return sha256.hexdigest()

# Пример использования
# file_hash = hash_file('document.pdf')
# print(f"Хеш файла — {file_hash}")
