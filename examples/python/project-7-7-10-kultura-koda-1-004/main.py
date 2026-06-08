class User:
    """Пользователь системы."""

    def __init__(self, name: str, age: int):
        """
        :param name: отображаемое имя
        :param age: возраст в полных годах
        """
        self.name = name
        self.age = age

    def is_adult(self) -> bool:
        """True, если возраст ≥ 18."""
        return self.age >= 18
