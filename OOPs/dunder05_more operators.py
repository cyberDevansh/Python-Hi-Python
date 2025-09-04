class Number:
    def __init__(self, value):
        self.value = value

    def __and__(self, other):   # a & b
        return Number(self.value & other.value)

    def __or__(self, other):    # a | b
        return Number(self.value | other.value)

    def __xor__(self, other):   # a ^ b
        return Number(self.value ^ other.value)

    def __lshift__(self, other):  # a << b
        return Number(self.value << other.value)

    def __rshift__(self, other):  # a >> b
        return Number(self.value >> other.value)

    def __invert__(self):       # ~a (unary operator)
        return Number(~self.value)

    def __str__(self):
        return str(self.value)



a = Number(10)   # binary 1010
b = Number(3)    # binary 0011

print("AND:", a & b)       # 10 & 3 = 2
print("OR:", a | b)        # 10 | 3 = 11
print("XOR:", a ^ b)       # 10 ^ 3 = 9
print("Left Shift:", a << b)  # 10 << 3 = 80
print("Right Shift:", a >> b) # 10 >> 3 = 1
print("Invert (~a):", ~a)     # ~10 = -11
