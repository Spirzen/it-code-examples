import array
import math
import pygame


def _sine_wave(freq: float, duration: float, volume: float = 0.25) -> pygame.mixer.Sound:
    rate = 22050
    n = int(rate * duration)
    buf = array.array("h")
    for i in range(n):
        t = i / rate
        fade = min(1.0, i / (rate * 0.01), (n - i) / (rate * 0.04))
        val = int(32767 * volume * fade * math.sin(2 * math.pi * freq * t))
        buf.append(val)
    return pygame.mixer.Sound(buffer=buf)


class AudioSystem:
    def __init__(self) -> None:
        self.enabled = False
        try:
            if not pygame.mixer.get_init():
                pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)
            self._sfx = {
                "swing": _sine_wave(180, 0.07, 0.12),
                "kill": _sine_wave(90, 0.15, 0.2),
                "level_up": _sine_wave(440, 0.25, 0.25),
            }
            self.enabled = True
        except Exception:
            pass

    def play(self, name: str) -> None:
        if self.enabled and name in self._sfx:
            self._sfx[name].play()
