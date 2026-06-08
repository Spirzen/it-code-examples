class Meta(type):
    def __new__(mcs, name, bases, namespace):
        print(f"Создаём класс {name} через метакласс {mcs.__name__}")
        namespace['created_by_meta'] = True
        return super().__new__(mcs, name, bases, namespace)
    
    def __init__(cls, name, bases, namespace):
        print(f"Инициализируем класс {name}")
        super().__init__(name, bases, namespace)

class MyClass(metaclass=Meta):
    value = 42

print(MyClass.created_by_meta)  # True
print(type(MyClass))            # <class '__main__.Meta'>
