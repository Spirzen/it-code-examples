from kivy.app import App
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class GameScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", padding=dp(8), spacing=dp(8), **kwargs)
        self.add_widget(Label(text="Snake", font_size=dp(24)))
        self.add_widget(Button(text="Start"))


class SnakeApp(App):
    def build(self):
        return GameScreen()


if __name__ == "__main__":
    SnakeApp().run()
