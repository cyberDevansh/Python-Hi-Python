class Person:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):   # getter
        return self._age

    @age.setter   #so ghere setter is keyword not just convention 
    def age(self, value):   # setter
        if value < 0:
            print("Age cannot be negative")
        else:
            self._age = value

p = Person(20)
print(p.age)   #  looks like direct access, but calls getter
p.age = -5     #  calls setter, rejects
print(p.age)   #  still 20






# ✅ So in short:
# @property → defines the getter.
# @age.setter → links a setter to that same property.
# They work together under one name (age), instead of two separate functions.