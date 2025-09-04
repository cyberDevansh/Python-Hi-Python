class Number:
    def __init__(self, value):
        self.value = value         

    def __add__(self, other):
        return Number(self.value + other.value)

a = Number(10)
b = Number(20)
c = a + b  # c = a + b → calls Number.__add__(a, b)
print(c.value)   

