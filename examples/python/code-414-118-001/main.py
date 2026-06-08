def register_user(email, age):
    if email is None:
        raise ValueError("email обязателен")
    if not isinstance(email, str):
        raise TypeError("email должен быть строкой")
    if not email.strip():
        raise ValueError("email не может быть пустым")

    if not isinstance(age, int):
        raise TypeError("age должен быть int")
    if age < 0 or age > 150:
        raise ValueError("age вне допустимого диапазона")

    # дальше — сохранение в базу
    return {"email": email.strip(), "age": age}
