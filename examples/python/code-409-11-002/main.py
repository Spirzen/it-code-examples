# Абстракция (интерфейс) - то, от чего зависят оба
class DatabaseInterface:
    def save(self, Данные):
        raise NotImplementedError

# Модуль Б (деталь) зависит от абстракции
class PostgresDB(DatabaseInterface):
    def save(self, Данные):
        print(f"Сохраняю {Данные} в PostgreSQL")

class MySQLDB(DatabaseInterface):
    def save(self, Данные):
        print(f"Сохраняю {Данные} в MySQL")

# Модуль А (бизнес-логика) тоже зависит от абстракции
class UserService:
    def __init__(self, db: DatabaseInterface):  # ✅ получает абстракцию извне
        self.db = db
    
    def register(self, name):
        self.db.save(name)

# Пользуемся
postgres = PostgresDB()
service = UserService(postgres)  # можно отдать любую БД
service.register("Алексей")

mysql = MySQLDB()
service2 = UserService(mysql)  # тот же код, другая БД
service2.register("Мария")
