class Person:
    def __init__(self, name):
        self._name = name   # the underscore (convention for private)

    def get_name(self):    #getter 
        return self._name

    def set_name(self, value):        #setter
        self._name = value

p = Person("Ramesh")

print(p.get_name())  
p.set_name("Suresh")
print(p.get_name())
