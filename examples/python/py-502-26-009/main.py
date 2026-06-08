class Widget:
    default_color = "gray"
    
    def __init__(self, name):
        self.name = name
        self.color = Widget.default_color
    
    def render(self):
        return f"<{self.name} color='{self.color}'>"

w = Widget("button")
print(w.name)      # button (атрибут экземпляра)
print(w.color)     # gray (атрибут экземпляра, инициализированный из класса)
print(w.render())  # <button color='gray'>
