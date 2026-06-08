import tkinter as tk

def update_status():
    parts = []
    if notify_var.get():
        parts.append("уведомления")
    if sound_var.get():
        parts.append("звук")
    role = role_var.get()
    status_var.set(
        f"Роль: {role}; включено: {', '.join(parts) or 'ничего'}"
    )

root = tk.Tk()
root.title("Настройки")
frame = tk.Frame(root, padx=16, pady=16)
frame.pack()

notify_var = tk.BooleanVar(value=True)   # True/False для Checkbutton
sound_var = tk.BooleanVar(value=False)
role_var = tk.StringVar(value="user")    # одна строка для группы Radiobutton

tk.Checkbutton(frame, text="Уведомления", variable=notify_var, command=update_status).pack(anchor="w")
tk.Checkbutton(frame, text="Звук", variable=sound_var, command=update_status).pack(anchor="w")

tk.Label(frame, text="Роль:").pack(anchor="w", pady=(12, 0))
tk.Radiobutton(frame, text="Пользователь", variable=role_var, value="user", command=update_status).pack(anchor="w")
tk.Radiobutton(frame, text="Администратор", variable=role_var, value="admin", command=update_status).pack(anchor="w")

status_var = tk.StringVar()
tk.Label(frame, textvariable=status_var, fg="gray").pack(anchor="w", pady=(12, 0))
update_status()  # начальная подпись при старте

root.mainloop()
