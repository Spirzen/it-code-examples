# Пример использования SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

engine = create_engine('sqlite:///example.db')
Session = sessionmaker(bind=engine)
session = Session()

# Создание таблицы
Base.metadata.create_all(engine)

# Добавление записи
user = User(name='Иван', email='ivan@example.com')
session.add(user)
session.commit()
