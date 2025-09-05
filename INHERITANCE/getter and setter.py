class Person:
    def __init__(self, name):
        self._name = name   # note the underscore (convention for private)

    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value

p = Person("Ramesh")

print(p.get_name())   # call getter
p.set_name("Suresh")  # call setter
print(p.get_name())
