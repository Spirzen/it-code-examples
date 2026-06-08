import tkinter as tk
from tkinter import filedialog, messagebox

root = tk.Tk()
root.title("Блокнот")
root.geometry("480x360")

text = tk.Text(root, wrap=tk.WORD)
text.pack(fill=tk.BOTH, expand=True)

current_file = {"path": None}

def load_file():
    path = filedialog.askopenfilename(filetypes=[("Текст", "*.txt"), ("Все", "*.*")])
    if not path:
        return
    with open(path, encoding="utf-8") as f:
        text.delete("1.0", tk.END)
        text.insert("1.0", f.read())
    current_file["path"] = path
    root.title(f"Блокнот — {path}")

def save_file():
    path = current_file["path"] or filedialog.asksaveasfilename(defaultextension=".txt")
    if not path:
        return
    with open(path, "w", encoding="utf-8") as f:
        f.write(text.get("1.0", tk.END))
    current_file["path"] = path
    messagebox.showinfo("Сохранено", f"Файл записан:\n{path}")

menubar = tk.Menu(root)
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Открыть", command=load_file)
file_menu.add_command(label="Сохранить", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=root.destroy)
menubar.add_cascade(label="Файл", menu=file_menu)
root.config(menu=menubar)

root.mainloop()
