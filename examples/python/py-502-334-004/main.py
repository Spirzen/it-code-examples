    def apply_filter(self) -> None:
        if self.df is None:
            return

        query = self.search_var.get().strip().lower()
        if not query:
            self.populate_table(self.df)
            self.set_status(f"Загружено: {len(self.df)} строк")
            return

        mask = self.df.astype(str).apply(
            lambda col: col.str.lower().str.contains(query, na=False)
        ).any(axis=1)
        filtered = self.df[mask]
        self.populate_table(filtered)
        self.set_status(f"Найдено: {len(filtered)} из {len(self.df)} строк")

    def reset_filter(self) -> None:
        self.search_var.set("")
        if self.df is not None:
            self.populate_table(self.df)
            self.set_status(f"Загружено: {len(self.df)} строк")
