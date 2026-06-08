from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class PingPongApp(App):
    def build(self):
        Window.clearcolor = (0.05, 0.06, 0.08, 1)
        root = BoxLayout(orientation="vertical", padding=12, spacing=8)
        root.add_widget(Label(text="Pong", font_size="24sp"))
        return root


if __name__ == "__main__":
    PingPongApp().run()
