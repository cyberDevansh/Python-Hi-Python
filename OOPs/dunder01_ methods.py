# Dunder = Double UNDERscore (two underscores at start and end).
# Example: __init__, __str__, __len__, __add__ etc.
# These are special methods in Python which have a fixed meaning and are called automatically in certain situations.
# Also called “magic methods”.

class Employee:
    def __init__(self, name):
        self.name = name
        print("Object created!")

p = Employee("Guppe")
