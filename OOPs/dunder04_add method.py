class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

a = Number(10) # Calls Number.__init__(self=let it be objA, value=10)
b = Number(20)
print(a + b)  
c=a+b
print(c)
# either we can write print(Number(10)+Number(50))

#Each instance keeps its own attributes in its internal dict. You can check:
print(a.__dict__)  
print(b.__dict__)
# So:
# self.value means “look up value on the self object (the left operand).”
# other.value means “look up value on the other object (the right operand).”



#Python calls Number.__add__(self=a, other=b).
# self → the left operand (a / objA).
# other → the right operand (b / objB).
# Reads self.value (10) from a and other.value (20) from b.
# Returns 10 + 20 = 30 (a plain int).
