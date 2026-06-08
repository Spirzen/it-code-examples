import tkinter as tk

def add_task():
    text = entry.getstrip()
    if text:
        listbox.insert(tk.END, text)      # tk.END — в конец списка
        entry.delete(0, tk.END)          # очистить поле ввода

def remove_task():
    sel = listbox.curselection()         # кортеж индексов выделенных строк
    if sel:
        listbox.delete(sel[0])

root = tk.Tk()
root.title("Список задач")
root.geometry("320x280")

frame = tk.Frame(root, padx=12, pady=12)
frame.pack(fill=tk.BOTH, expand=True)

entry = tk.Entry(frame)
entry.pack(fill=tk.X)
entry.bind("<Return>", lambda e: add_task())

btn_row = tk.Frame(frame)
btn_row.pack(fill=tk.X, pady=(8, 8))
tk.Button(btn_row, text="Добавить", command=add_task).pack(side=tk.LEFT, padx=(0, 4))
tk.Button(btn_row, text="Удалить", command=remove_task).pack(side=tk.LEFT)

listbox = tk.Listbox(frame, height=10)
listbox.pack(fill=tk.BOTH, expand=True)

root.mainloop()
