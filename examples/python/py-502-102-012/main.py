
import shutil
import os

def check_disk_usage(path='/'):
    total, used, free = shutil.disk_usage(path)
    
    percent_free = (free / total) * 100
    
    print(f"\nДиск: {path}")
    print(f"Всего: {total // (2**30)} GB")
    print(f"Занято: {used // (2**30)} GB")
    print(f"Свободно: {free // (2**30)} GB")
    print(f"Свободно (%): {percent_free:.2f}%")
    
    if percent_free < 20:
        print("Внимание: Свободного места менее 20%!")

if __name__ == "__main__":
    root_path = "/" if os.name != 'nt' else "C:\\"
    check_disk_usage(root_path)
