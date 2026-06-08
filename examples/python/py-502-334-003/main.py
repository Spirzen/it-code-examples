    def populate_table(self, df: pd.DataFrame) -> None:
        self.tree.delete(*self.tree.get_children())
        self.tree["columns"] = list(df.columns)

        for col in df.columns:
            self.tree.heading(col, text=str(col))
            self.tree.column(col, width=120, anchor=tk.W, minwidth=60)

        display_df = df.head(1000)
        for _, row in display_df.iterrows():
            values = ["" if pd.isna(v) else str(v) for v in row]
            self.tree.insert("", tk.END, values=values)

        if len(df) > 1000:
            self.set_status(
                f"Показано 1000 из {len(df)} строк. Используйте поиск для фильтрации."
            )
