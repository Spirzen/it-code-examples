
import subprocess
import platform

def list_processes():
    system = platform.system()
    command = []
    
    if system == "Windows":
        command = ["tasklist"]
    else:
        command = ["ps", "-ef"]
        
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        print(f"ОС: {system}\n")
        print(result.stdout[:1000]) # Ограничение вывода для краткости
    except subprocess.CalledProcessError as e:
        print(f"Ошибка выполнения команды: {e}")
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    list_processes()
