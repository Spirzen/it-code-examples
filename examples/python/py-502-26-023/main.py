class Smartphone:
    def __init__(self, brand, model, battery=100):
        self.brand = brand      # Производитель
        self.model = model      # Модель
        self.__battery = battery  # Заряд (скрытое поле)
        self.is_on = True       # Включен ли

    def call(self, minutes):
        if self.__battery <= 0:
            print("Телефон разряжен!")
            return
        cost = minutes * 2  # 2% заряда в минуту
        self.__battery -= cost
        if self.__battery < 0:
            self.__battery = 0
        print(f"Поговорили {minutes} мин. Заряд: {self.__battery}%")

    def charge(self):
        self.__battery = 100
        print(f"{self.brand} {self.model} полностью заряжен!")

    def show_status(self):
        status = "Включен" if self.is_on else "Выключен"
        print(f"{self.brand} {self.model} | {status} | Заряд: {self.__battery}%")


# Используем
iphone = Smartphone("Apple", "iPhone 15")
iphone.show_status()    # Apple iPhone 15 | Включен | Заряд: 100%
iphone.call(30)         # Поговорили 30 мин. Заряд: 40%
iphone.call(25)         # Поговорили 25 мин. Заряд: 0%
iphone.call(5)          # Телефон разряжен!
iphone.charge()         # Apple iPhone 15 полностью заряжен!
