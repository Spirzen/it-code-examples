class Автомобиль:
    def __init__(self):
        self._model = ""
        self._year = 0

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        if not value:
            raise ValueError("Модель не может быть пустой!")
        self._model = value
