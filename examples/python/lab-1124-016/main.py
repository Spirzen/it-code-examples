import tkinter as tk

root = tk.Tk()
root.title("Контекстное меню")

text = tk.Text(root, height=8, width=40)
text.pack(padx=12, pady=12)
text.insert("1.0", "Щёлкните правой кнопкой мыши по полю.")

menu = tk.Menu(root, tearoff=0)
menu.add_command(
    label="Копировать",
    command=lambda: root.clipboard_clear()
    or root.clipboard_append(text.get("sel.first", "sel.last") if text.tag_ranges("sel") else ""),
)
menu.add_command(label="Вставить", command=lambda: text.insert(tk.INSERT, root.clipboard_get()))
menu.add_separator()
menu.add_command(label="Очистить", command=lambda: text.delete("1.0", tk.END))

def show_menu(event):
    menu.tk_popup(event.x_root, event.y_root)

text.bind("<Button-3>", show_menu)  # ПКМ; на macOS иногда <Button-2>

root.mainloop()
