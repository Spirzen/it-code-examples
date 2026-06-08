    def show_stats(self) -> None:
        if self.df is None:
            messagebox.showinfo("Статистика", "Сначала откройте файл с данными.")
            return

        info = [
            f"Строк: {len(self.df)}",
            f"Столбцов: {len(self.df.columns)}",
            "",
            "Типы данных:",
            self.df.dtypes.to_string(),
            "",
            "Описательная статистика (числовые столбцы):",
        ]

        numeric = self.df.select_dtypes(include="number")
        if numeric.empty:
            info.append("  (числовых столбцов нет)")
        else:
            info.append(numeric.describe().to_string())

        messagebox.showinfo("Статистика", "\n".join(info))
