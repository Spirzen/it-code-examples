import tkinter as tk

root = tk.Tk()
root.title("Секундомер")
root.geometry("200x120")

elapsed = {"sec": 0}
running = {"active": False}

time_var = tk.StringVar(value="00:00")

def tick():
    if running["active"]:
        elapsed["sec"] += 1
        m, s = divmod(elapsed["sec"], 60)
        time_var.set(f"{m:02d}:{s:02d}")
        root.after(1000, tick)

def start():
    if not running["active"]:
        running["active"] = True
        tick()

def stop():
    running["active"] = False

def reset():
    running["active"] = False
    elapsed["sec"] = 0
    time_var.set("00:00")

tk.Label(root, textvariable=time_var, font=("Consolas", 24)).pack(pady=(16, 8))
row = tk.Frame(root)
row.pack()
tk.Button(row, text="Старт", command=start).pack(side=tk.LEFT, padx=4)
tk.Button(row, text="Стоп", command=stop).pack(side=tk.LEFT, padx=4)
tk.Button(row, text="Сброс", command=reset).pack(side=tk.LEFT, padx=4)

root.mainloop()
