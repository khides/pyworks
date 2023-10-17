
class IntBox:
    def __init__(self, value) -> None:
        self.value = value

a = IntBox(1)
b = a
a.value = 2
print(a.value)