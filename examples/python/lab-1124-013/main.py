import tkinter as tk

ALL_ITEMS = ["Яблоко", "Абрикос", "Банан", "Ананас", "Груша", "Алыча"]

def filter_list(*_):
    query = search_var.getlower()
    listbox.delete(0, tk.END)
    for item in ALL_ITEMS:
        if query in item.lower():
            listbox.insert(tk.END, item)

root = tk.Tk()
root.title("Поиск")
root.geometry("260x280")

frame = tk.Frame(root, padx=12, pady=12)
frame.pack(fill=tk.BOTH, expand=True)

search_var = tk.StringVar()
search_var.trace_add("write", filter_list)
tk.Entry(frame, textvariable=search_var).pack(fill=tk.X)
listbox = tk.Listbox(frame, height=12)
listbox.pack(fill=tk.BOTH, expand=True, pady=(8, 0))

filter_list()  # показать весь список при старте
root.mainloop()
