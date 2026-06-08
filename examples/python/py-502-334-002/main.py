    def open_file(self) -> None:
        path = filedialog.askopenfilename(
            title="Выберите файл",
            filetypes=[
                ("Таблицы", "*.csv *.xlsx *.xls"),
                ("CSV", "*.csv"),
                ("Excel", "*.xlsx *.xls"),
                ("Все файлы", "*.*"),
            ],
        )
        if not path:
            return

        try:
            if path.lower().endswith(".csv"):
                df = pd.read_csv(path)
            else:
                df = pd.read_excel(path)
        except Exception as exc:
            messagebox.showerror("Ошибка", f"Не удалось прочитать файл:\n{exc}")
            return

        self.df = df
        self.file_path = path
        self.search_var.set("")
        self.file_label.config(text=path, foreground="black")
        self.set_status(f"Загружено: {len(df)} строк, {len(df.columns)} столбцов")
