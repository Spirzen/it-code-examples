
import os

def scan_directory(path, depth=0):
    max_depth = 3  # Ограничение глубины для наглядности
    
    if depth > max_depth:
        return
        
    indent = "  " * depth
    items = os.listdir(path)
    
    for item in sorted(items):
        full_path = os.path.join(path, item)
        if os.path.isdir(full_path):
            print(f"{indent}[DIR]  {item}/")
            scan_directory(full_path, depth + 1)
        else:
            size = os.path.getsize(full_path)
            print(f"{indent}[FILE] {item} ({size} байт)")

if __name__ == "__main__":
    directory = "."
    scan_directory(directory)
