import tkinter as tk
from tkinter import ttk


class DataViewerApp:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Pandas Data Viewer")
        self.root.geometry("900x600")
        self.root.minsize(700, 400)

        self.df = None
        self.file_path = None

        self._build_ui()

    def _build_ui(self) -> None:
        toolbar = ttk.Frame(self.root, padding=8)
        toolbar.pack(fill=tk.X)

        ttk.Button(toolbar, text="Открыть файл", command=self.open_file).pack(
            side=tk.LEFT, padx=(0, 8)
        )
        ttk.Button(toolbar, text="Статистика", command=self.show_stats).pack(
            side=tk.LEFT, padx=(0, 8)
        )

        self.file_label = ttk.Label(toolbar, text="Файл не выбран", foreground="gray")
        self.file_label.pack(side=tk.LEFT, padx=8)

        filter_frame = ttk.Frame(self.root, padding=(8, 0, 8, 8))
        filter_frame.pack(fill=tk.X)

        ttk.Label(filter_frame, text="Поиск:").pack(side=tk.LEFT)
        self.search_var = tk.StringVar()
        ttk.Entry(filter_frame, textvariable=self.search_var, width=40).pack(
            side=tk.LEFT, padx=8
        )
        ttk.Button(filter_frame, text="Сбросить", command=self.reset_filter).pack(
            side=tk.LEFT
        )

        table_frame = ttk.Frame(self.root, padding=8)
        table_frame.pack(fill=tk.BOTH, expand=True)

        self.tree = ttk.Treeview(table_frame, show="headings")
        vsb = ttk.Scrollbar(table_frame, orient=tk.VERTICAL, command=self.tree.yview)
        hsb = ttk.Scrollbar(table_frame, orient=tk.HORIZONTAL, command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        self.tree.grid(row=0, column=0, sticky="nsew")
        vsb.grid(row=0, column=1, sticky="ns")
        hsb.grid(row=1, column=0, sticky="ew")
        table_frame.rowconfigure(0, weight=1)
        table_frame.columnconfigure(0, weight=1)

        self.status = ttk.Label(self.root, text="Готово", padding=8, relief=tk.SUNKEN)
        self.status.pack(fill=tk.X, side=tk.BOTTOM)

    def open_file(self) -> None:
        self.set_status("Кнопка «Открыть файл» — на этапе 2")

    def show_stats(self) -> None:
        self.set_status("Кнопка «Статистика» — на этапе 5")

    def reset_filter(self) -> None:
        self.search_var.set("")

    def set_status(self, text: str) -> None:
        self.status.config(text=text)


def main() -> None:
    root = tk.Tk()
    DataViewerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
