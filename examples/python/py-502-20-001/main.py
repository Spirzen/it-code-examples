x = "глобальный"

def outer():
    x = "обрамляющий"
    
    def inner():
        x = "локальный"
        print(x)  # -> "локальный"
    
    inner()
    print(x)      # -> "обрамляющий"

outer()
print(x)          # -> "глобальный"
