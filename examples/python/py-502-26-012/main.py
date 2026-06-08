class A:
    def __init__(self):
        self._internal = 42
        self.__mangled = "hidden"

class B(A):
    def __init__(self):
        super().__init__()
        self.__mangled = "also hidden in B"

b = B()
print(b._internal)           # 42
print(b._A__mangled)         # "hidden"
print(b._B__mangled)         # "also hidden in B"
