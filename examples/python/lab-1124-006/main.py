import tkinter as tk

root = tk.Tk()
root.title("Grid-форма")
root.geometry("360x160")

frame = tk.Frame(root, padx=12, pady=12)
frame.pack(fill=tk.BOTH, expand=True)
frame.grid_columnconfigure(1, weight=1)  # вторая колонка растягивается

tk.Label(frame, text="Email:").grid(row=0, column=0, sticky="w", pady=4)
email = tk.Entry(frame)
email.grid(row=0, column=1, sticky="ew", padx=(8, 0), pady=4)

tk.Label(frame, text="Пароль:").grid(row=1, column=0, sticky="w", pady=4)
password = tk.Entry(frame, show="*")  # show="*" — маскировка пароля
password.grid(row=1, column=1, sticky="ew", padx=(8, 0), pady=4)

tk.Button(frame, text="Войти").grid(row=2, column=1, sticky="e", pady=(12, 0))

root.mainloop()
