    def _on_press(self, event: tk.Event) -> None:
        self.last_x, self.last_y = event.x, event.y
        self._draw_point(event.x, event.y)

    def _on_drag(self, event: tk.Event) -> None:
        if self.last_x is None or self.last_y is None:
            return
        self.canvas.create_line(
            self.last_x,
            self.last_y,
            event.x,
            event.y,
            fill="white",
            width=BRUSH_WIDTH,
            capstyle=tk.ROUND,
            smooth=True,
        )
        self.draw.line(
            [self.last_x, self.last_y, event.x, event.y],
            fill=DRAW_COLOR,
            width=BRUSH_WIDTH,
        )
        self.last_x, self.last_y = event.x, event.y

    def _on_release(self, _event: tk.Event) -> None:
        self.last_x, self.last_y = None, None

    def _draw_point(self, x: int, y: int) -> None:
        r = BRUSH_WIDTH // 2
        self.canvas.create_oval(x - r, y - r, x + r, y + r, fill="white", outline="white")
        self.draw.ellipse([x - r, y - r, x + r, y + r], fill=DRAW_COLOR)

    def _clear(self) -> None:
        self.canvas.delete("all")
        self.image = Image.new("L", (CANVAS_SIZE, CANVAS_SIZE), BACKGROUND_COLOR)
        self.draw = ImageDraw.Draw(self.image)
        if self.model is not None:
            self.result_var.set("Результат появится здесь")
