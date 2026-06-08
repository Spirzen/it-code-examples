
import sys

with open(sys.argv[1], 'rb') as f:
    data = f.read()

# Ищем MZ (0x4d, 0x5a)
for key in range(256):
    if data[0] ^ key == 0x4d and data[1] ^ key == 0x5a:
        print(f"Possible XOR key: 0x{key:02x}")
        # Расшифровываем и сохраняем
        decrypted = bytes(b ^ key for b in data)
        with open(f'decrypted_{key:02x}', 'wb') as out:
            out.write(decrypted)
        break
