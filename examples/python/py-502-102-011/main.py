
import os
import shutil

from datetime import datetime

def create_backup(source_dir, backup_dir):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"backup_{timestamp}"
    backup_path = os.path.join(backup_dir, backup_name)
    
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
        
    try:
        shutil.copytree(source_dir, backup_path)
        print(f"Резервная копия создана: {backup_path}")
    except FileExistsError:
        print("Ошибка: Резервная копия с таким именем уже существует.")
    except Exception as e:
        print(f"Ошибка копирования: {e}")

if __name__ == "__main__":
    source = "./my_project"
    destination = "./backups"
    create_backup(source, destination)
