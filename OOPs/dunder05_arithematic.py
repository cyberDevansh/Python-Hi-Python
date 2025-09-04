class Number:
    def __init__(self, value):
        self.value = value
    
    def __add__(self,other):
        return Number(self.value + other.value)

    def __sub__(self, other):  
        return Number(self.value - other.value)

    def __mul__(self, other):   # a * b
        return Number(self.value * other.value)

    def __truediv__(self, other):   # a / b
        return Number(self.value / other.value)

    def __floordiv__(self, other):  # a // b
        return Number(self.value // other.value)

    def __mod__(self, other): 
        return Number(self.value % other.value)

    def __pow__(self, other):   # a ** b
        return Number(self.value ** other.value)

    # For easy printing
    def __str__(self):
        return str(self.value)



a = Number(10)
b = Number(3)

print("Add:", a + b)     
print("Subtraction:", a - b)     
print("Multiplication:", a * b)   
print("True Division:", a / b)    
print("Floor Division:", a // b)  # 10 // 3 = 3
print("Modulus:", a % b)          
print("Power:", a ** b)           
