    def _start_training(self) -> None:
        self.result_var.set("Первый запуск: обучение модели на MNIST (~1–2 мин)...")
        self.progress.grid()
        self.progress.start(12)

        def worker() -> None:
            try:
                train(on_progress=lambda msg: self.root.after(0, self.result_var.set, msg))
                self.root.after(0, self._on_training_done)
            except Exception as exc:
                self.root.after(0, self._on_training_failed, str(exc))

        threading.Thread(target=worker, daemon=True).start()

    def _on_training_done(self) -> None:
        self.progress.stop()
        self.progress.grid_remove()
        self._load_model()

    def _on_training_failed(self, error: str) -> None:
        self.progress.stop()
        self.progress.grid_remove()
        messagebox.showerror("Ошибка обучения", error)
        self.root.destroy()

    def _predict(self) -> None:
        if self.model is None:
            return

        resized = self._preprocess()
        if resized is None:
            self.result_var.set("Сначала нарисуйте цифру")
            return

        transform = transforms.Compose(
            [
                transforms.ToTensor(),
                transforms.Normalize((0.1307,), (0.3081,)),
            ]
        )
        tensor = transform(resized).unsqueeze(0).to(self.device)

        with torch.no_grad():
            logits = self.model(tensor)
            probs = F.softmax(logits, dim=1)[0]
            digit = int(probs.argmax().item())
            confidence = float(probs[digit].item()) * 100

        top3 = probs.topk(3)
        details = ", ".join(
            f"{int(idx.item())}: {prob.item() * 100:.1f}%"
            for prob, idx in zip(top3.values, top3.indices)
        )
        self.result_var.set(f"Цифра: {digit}  ({confidence:.1f}%)  ·  топ-3: {details}")
