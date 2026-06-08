from pathlib import Path

p = Path('/home/user/docs/file.txt')

print(p.name)           # 'file.txt'
print(p.suffix)         # '.txt'
print(p.stem)           # 'file'
print(p.parent)         # PosixPath('/home/user/docs')
print(p.exists())       # True/False
print(p.is_file())      # Проверка типа

# Сборка путей
new_path = p.parent / 'backup' / p.name
print(new_path)         # /home/user/docs/backup/file.txt

# Поиск файлов по шаблону
for pyfile in Path('.').glob('*.py'):
    print(pyfile)
