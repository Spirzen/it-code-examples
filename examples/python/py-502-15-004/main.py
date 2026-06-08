# Глубокая вложенность
def validate_user(user):
    if user is not None:
        if user.is_active:
            if user.email_verified:
                if user.age >= 18:
                    return True
    return False

# Плоская структура с гвардами
def validate_user(user):
    if user is None:
        return False
    if not user.is_active:
        return False
    if not user.email_verified:
        return False
    if user.age < 18:
        return False
    return True
