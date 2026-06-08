import tkinter as tk

def center_window(root, width, height):
    root.update_idletasks()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f"{width}x{height}+{x}+{y}")

def create_app(title="Tkinter App", width=640, height=480):
    root = tk.Tk()
    root.title(title)
    center_window(root, width, height)
    root.minsize(320, 240)
    return root

if __name__ == "__main__":
    app = create_app("Моё приложение")
    tk.Label(app, text="Окно по центру экрана").pack(expand=True)
    app.mainloop()
