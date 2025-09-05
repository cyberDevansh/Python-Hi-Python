class Person:
    def __init__(self, age):
        self._age = age   # convention: _ means "internal/private"

    def get_age(self):    # getter
        return self._age

    def set_age(self, value):   # setter
        if value < 0:
            print("Age cannot be negative!")
        else:
            self._age = value

p = Person(20)

print(p.get_age()) 
p.set_age(-5)       
print(p.get_age())  
