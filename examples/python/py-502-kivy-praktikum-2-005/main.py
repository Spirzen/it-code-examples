def on_touch_down(self, touch):
    if not self.collide_point(*touch.pos):
        return super().on_touch_down(touch)
    self.player_touch_active = True
    self.player.x = self._clamp_paddle_x(
        touch.x - self.player.width / 2, self.player
    )
    return True

def on_touch_move(self, touch):
    if self.player_touch_active:
        self.player.x = self._clamp_paddle_x(
            touch.x - self.player.width / 2, self.player
        )
        return True
    return super().on_touch_move(touch)

def on_touch_up(self, touch):
    if self.player_touch_active:
        self.player_touch_active = False
        return True
