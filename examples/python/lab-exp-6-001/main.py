import random
import secrets

random.seed(42)                  # воспроизводимый PRNG
print(random.randint(1, 10))

secure_token = secrets.token_hex(16)  # CSPRNG
print(secure_token)
