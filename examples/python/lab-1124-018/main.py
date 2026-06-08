import tkinter as tk

def open_settings():
    dialog = tk.Toplevel(root)       # дочернее окно, не второй tk.Tk()!
    dialog.title("Настройки")
    dialog.geometry("280x140")
    dialog.transient(root)           # всегда поверх главного
    dialog.grab_set()                # модальность — ввод только здесь

    tk.Label(dialog, text="Имя пользователя:").pack(anchor="w", padx=12, pady=(12, 0))
    entry = tk.Entry(dialog, width=30)
    entry.pack(padx=12, pady=4)
    entry.focus_set()

    def close():
        dialog.grab_release()
        dialog.destroy()

    tk.Button(dialog, text="OK", command=close).pack(pady=12)

root = tk.Tk()
root.title("Главное окно")
tk.Button(root, text="Настройки", command=open_settings).pack(expand=True, pady=40)
root.mainloop()
