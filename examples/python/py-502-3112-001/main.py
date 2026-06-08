def create_tooltip(widget, text):
    tip = {"win": None}

    def enter(_):
        x, y, _, h = widget.bbox("insert") or (0, 0, 0, 0)
        x += widget.winfo_rootx() + 20
        y += widget.winfo_rooty() + h + 4
        tip["win"] = tw = tk.Toplevel(widget)
        tw.wm_overrideredirect(True)
        tw.geometry(f"+{x}+{y}")
        tk.Label(tw, text=text, bg="#ffffe0", relief=tk.SOLID, borderwidth=1).pack()

    def leave(_):
        if tip["win"]:
            tip["win"].destroy()
            tip["win"] = None

    widget.bind("<Enter>", enter)
    widget.bind("<Leave>", leave)

create_tooltip(btn, "Сохранить документ на диск")
