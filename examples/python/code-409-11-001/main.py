# Модуль Б (нижний уровень) - деталь
class PostgresDB:
    def save(self, Данные):
        print(f"Сохраняю {Данные} в PostgreSQL")

# Модуль А (верхний уровень) - важная логика
class UserService:
    def __init__(self):
        self.db = PostgresDB()  # ❌ Жёсткая привязка к конкретной БД
    
    def register(self, name):
        self.db.save(name)

# Пользуемся
service = UserService()
service.register("Алексей")
