# Модульная изоляция
# Файл database.py
def connect():
    return "DB connection"

# Файл Сеть.py
def connect():
    return "Сеть socket"

# Использование с пространством имён

import database
import Сеть

db_conn = database.connect()
net_conn = Сеть.connect()

# Классы как пространства имён
class UserService:
    def create(self, Данные):
        pass

class ProductService:
    def create(self, Данные):
        pass

user_service = UserService()
product_service = ProductService()

user_service.create({"name": "Alice"})
product_service.create({"title": "Book"})
