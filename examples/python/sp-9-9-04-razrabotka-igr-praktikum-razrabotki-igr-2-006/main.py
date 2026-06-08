    def start_swap_animation(self, x1, y1, x2, y2, on_complete):
        self.swap_anim = {
            "from": (x1, y1), "to": (x2, y2),
            "c1": self.grid[y1][x1], "c2": self.grid[y2][x2],
            "frame": SWAP_FRAMES, "callback": on_complete,
        }

    def try_swap(self, x1, y1, x2, y2):
        if self.swap_anim:
            return
        self.swap_tiles(x1, y1, x2, y2)

        def on_done():
            matches = self.find_matches()
            if matches:
                self.start_removal_animation(matches)  # этап 10
            else:
                self.swap_tiles(x1, y1, x2, y2)
                self.start_swap_animation(x2, y2, x1, y1, None)

        self.start_swap_animation(x1, y1, x2, y2, on_done)
