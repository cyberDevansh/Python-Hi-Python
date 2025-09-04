class Number:
    def __init__(self, value):
        self.value = value         

    def __add__(self, other):
        return Number(self.value + other.value)

    def __str__(self):
        return f"Number({self.value})"

a = Number(10)
b = Number(20)
c = a + b # this iss rread as 
# Number.__add__(a, b)
# → return Number(a.value + b.value)
# → return Number(10 + 20)
# → return Number(30)

print(c)    #Calls c.__str__(), which returns "Number(30)"
