from kivy.graphics import Color, RoundedRectangle
from kivy.metrics import dp
from kivy.uix.label import Label
from kivy.uix.widget import Widget

TILE_COLORS = {
    0: ("#cdc1b4", "#cdc1b4"),
    2: ("#eee4da", "#776e65"),
    4: ("#ede0c8", "#776e65"),
    # ... 8, 16, 32, ... 2048
}

class Tile(Widget):
    def set_value(self, value):
        self.value = value
        self._label.text = "" if value == 0 else str(value)
        bg, fg = TILE_COLORS.get(value, ("#3c3a32", "#f9f6f2"))
        # перерисовать RoundedRectangle и цвет текста
